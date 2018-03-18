import json
import re
import operator
import nltk
import string
import numpy as np
import os
import tweepy
import pandas as pd
from tweepy import OAuthHandler
from datetime import datetime
from collections import Counter

import matplotlib as mpl
import matplotlib.pyplot as plt

nltk.download("stopwords")  # download the stopword corpus on our computer
nltk.download("vader_lexicon")

from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

consumer_key = os.environ["CONSUMER_KEY_API"]
consumer_secret = os.getenv("CONSUMER_SECRET_API")
access_token = os.getenv("ACCESS_TOKEN_API")
access_secret = os.getenv("ACCESS_SECRET_API")

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)


searchString = input("Enter the word you want to analyse on twitter to have insights: ")

fname = searchString + '.json'


def writeToFile (filename, data):
    with open(filename, 'a') as f:
        f.write(json.dumps(data._json) + '\n')


api = tweepy.API(auth)

# Fetch Tweets
for tweet in tweepy.Cursor(api.search, q=searchString, lang="en").items(1500):
   writeToFile(fname, tweet)

sid = SIA()

sentiments = {"hour": [],  "positive": [], "neutral": [],  "negative": [], "total_tweets": []}
sentiment_list = {"positive": 0, "negative": 0, "neutral": 0}

with open(fname, 'r') as f:
    for line in f:
        tweet = json.loads(line)
        sentence = tweet['text']
        result = sid.polarity_scores(sentence)
        if result['compound'] > 0:
            sentiments["hour"].append(tweet['created_at'])
            sentiments["positive"].append(1)
            sentiments["negative"].append(0)
            sentiments["neutral"].append(0)
            sentiments["total_tweets"].append(1)
            sentiment_list["positive"] = sentiment_list["positive"] + 1
        elif result['compound'] == 0:
            sentiments["hour"].append(tweet['created_at'])
            sentiments["positive"].append(0)
            sentiments["negative"].append(0)
            sentiments["neutral"].append(1)
            sentiments["total_tweets"].append(1)
            sentiment_list["neutral"] = sentiment_list["neutral"] + 1
        else:
            sentiments["hour"].append(tweet['created_at'])
            sentiments["positive"].append(0)
            sentiments["negative"].append(1)
            sentiments["neutral"].append(0)
            sentiments["total_tweets"].append(1)
            sentiment_list["negative"] = sentiment_list["negative"] + 1

dfSentiments = pd.DataFrame(sentiments, columns=['hour', 'total_tweets', 'neutral', 'positive', 'negative'])
dfSentiments['hour'] = pd.to_datetime(dfSentiments['hour'])
dfSentiments.index = dfSentiments['hour']
del dfSentiments['hour']
print(dfSentiments.resample('30Min').sum())
plt.subplot(121)
labelsLine = ['total_tweets', 'neutral', 'positive', 'negative']
plt.plot(dfSentiments.resample('30Min').sum())
plt.legend(labelsLine)
plt.title('Insights on ' + searchString + ' with time')
plt.xlabel('Time (30 minutes)')
plt.ylabel('number of tweets')

# Pie chart, where the slices will be ordered and plotted counter-clockwise:

plt.subplot(122)
labels = ['Positive', 'Negative', 'Neutral']
sizes = [sentiment_list["positive"], sentiment_list["negative"], sentiment_list["neutral"]]
colors = ['green', 'red', 'orange']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.title('Sentimental Reaction of people on ' + searchString)
plt.savefig('Insights.png')  # Save it in a file
plt.show()                  # show it on IDE

