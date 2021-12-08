import pandas as pd
import praw 
import re 
import requests
import json
import csv
import time
import datetime

def get_unix_timestamp(date_string):
  '''
  Converts date 'YYYY-MM-DD' to Unix Time Stamp
  '''
  dt = pd.to_datetime(date_string)
  unix_timestamp = dt.replace(tzinfo=datetime.timezone.utc).timestamp()
  return round(unix_timestamp)


def get_daily_discussion_urls(subreddit, before_date, after_date):
  '''
  Returns dataframe of submission metadata given a subreddit (eg. 'wallstreetbets').

  Dates should be string-formatted 'YYYY-MM-DD'.
  * before_date: scrapes data before specified date (inclusive)
  * after_date: scrapes data after specified date (inclusive)

  Metadata: {id, title, url, date, flair}
  '''

  #function to get data from pushshift api
  def getPushshiftData(query, after, before, sub):
    url = 'https://api.pushshift.io/reddit/search/submission/?title='+str(query)+'&size=1000&after='+str(after)+'&before='+str(before)+'&subreddit='+str(sub)
    r = requests.get(url)
    data = json.loads(r.text)
    return data['data']

  #get relevant data from data extracted using previous function
  def collectSubData(subm):
    '''
    Extract metadata of each post 
    Metadata: id, title, url
    '''
    subData = [subm['id'], subm['title'], subm['url'], datetime.datetime.fromtimestamp(subm['created_utc']).date()]
    try:
        flair = subm['link_flair_text']
    except KeyError:
        flair = "NaN"
    subData.append(flair)
    subStats.append(subData)

  # Scrape Submission Metadata 
  sub = subreddit

  before = str(get_unix_timestamp(before_date)) # last date to extract data from
  after = str(get_unix_timestamp(after_date)) # first date to extract data from

  query = "Daily Discussion Thread"
  subCount = 0
  subStats = []

  data = getPushshiftData(query, after, before, sub)
  while len(data) > 0:
    try: 
      for submission in data:
          collectSubData(submission)
          subCount+=1

      after = data[-1]['created_utc']
      data = getPushshiftData(query, after, before, sub)

    except:
      continue
  # Push into DataFrame
  urls_df = pd.DataFrame(subStats, columns=['id','title','url','date','flair'])
  urls_df = urls_df[urls_df['flair']=='Daily Discussion']
  return urls_df

# Scrape Comments Using Submission URLs
def get_comments(urls_df, reddit_creds):
  '''
  Input your Reddit API credentials here in the form:
  reddit_creds = praw.Reddit(client_id='***', client_secret='***', user_agent='***', check_for_async=False)
  '''
  comments_by_submission = []
  for url in urls_df['url'].tolist():
    try:
      comments = []
      submission = reddit.submission(url=url)
      submission.comments.replace_more(limit=5)
      for comment in submission.comments.list():
          comments.append(comment.body)
    except:
      comments = None
    comments_by_submission.append(comments)
  return comments_by_submission

def comments_to_df(comments, urls_df):
  df_list = []
  for idx, comments in enumerate(comments):
    comments_df = pd.DataFrame(comments, columns=['comment'])
    comments_df['date'] = pd.to_datetime(urls_df['date'].iloc[idx])
    comments_df['title'] = urls_df['title'].iloc[idx]
    df_list.append(comments_df)

  merged_df = pd.concat(df_list)
  merged_df.to_csv('submission_comments.csv', index=False)
  return merged_df

