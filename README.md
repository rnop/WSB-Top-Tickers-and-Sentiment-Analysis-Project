# WSB-Top-Tickers-and-Sentiment-Analysis-Project

<a href="https://github.com/rnop/WSB-Top-Tickers-and-Sentiment-Analysis-Project/blob/main/Social%20Media%20Sentiment%20of%20Financial%20Groups.pdf" target="_blank">Research Paper (PDF) for Stanford Natural Language Understanding Course CS224U</a>

### Introduction
The following project looks to build an efficient pipeline that scrapes, pre-processes, and extracts sentiment from social media comments from r/WallStreetBets. Social media sentiment will be computed using traditional machine learning models, a rule-based lexicon model, and lastly, pre-trained and fine-tuned transformer models. The end goal is build an automated, efficient, and accurate sentiment pipeline that visualizes the daily, weekly, and monthly sentiment of popular stocks and major stock market indices.  

![alt text](https://github.com/rnop/WSB-Top-Tickers-and-Sentiment-Analysis-Project/blob/main/top_mentions.png)
![alt text](https://github.com/rnop/WSB-Top-Tickers-and-Sentiment-Analysis-Project/blob/main/GME_sentiment.png)

### Python Libraries
* numpy
* pandas
* matplotlib
* seaborn
* datetime
* praw (7.5.0)
* scipy
* sklearn
* transformers (4.13.0)
* emojis
* vaderSentiment

### Automated Sentiment Pipeline
1. Scrape Reddit comments
2. Pre-process comments
3. Serve to model endpoints to classify sentiment (Positive, Neutral, Negative)
4. Aggregate sentiment across individual tickers and major indices
5. Visualize daily, weekly, monthly sentiment 
