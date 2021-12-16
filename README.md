# WSB-Top-Tickers-and-Sentiment-Analysis-Project

### Introduction
r/WallStreetBets is a famous trading community on Reddit consisting of over 11 million users (as of Dec 2021). With so many users, it is very time consuming to parse through the subreddit and look at the hundreds of different posts and comments generated everyday. Therefore, the goal of this project was to efficiently automate this process to extract the most popularly discussed stocks and compute the sentiment of those stocks. 

![img]("https://raw.githubusercontent.com/rnop/WSB-Top-Tickers-and-Sentiment-Analysis-Project/main/top_mentions.png")

### Main Libraries
* python
* pandas
* matplotlib
* seaborn
* datetime
* praw (7.5.0)
* transformers (4.13.0)
* emojis
* vaderSentiment

### Step-By-Step Process
1. Scrape Reddit Comments and Stock Tickers
2. Compute the Most Popularly Discussed Stocks and Their Overall Sentiment
3. Visualize the Daily, Weekly, Monthly, and Yearly Sentiment of Stocks
