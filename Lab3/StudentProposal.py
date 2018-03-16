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

fname = 'Data.json'

searchString = input("Enter the word you want to analyse on twitter to have insights: ")

def writeToFile (filename, data):
    with open(filename, 'a') as f:
        f.write(json.dumps(data._json) + '\n')


api = tweepy.API(auth)


for tweet in tweepy.Cursor(api.search, q=searchString, lang="en").items(10):
    writeToFile(fname, tweet)

sid = SIA()

sentiments = {"hour": [],  "positive": [], "neutral": [],  "negative": [], "total_tweets": []}
sentiment_list = {"positive": 0, "negative": 0, "neutral": 0}


punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via', 'a', '…', 'q']
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
positiveTweets = dfSentiments.resample('30Min').agg({'positive': np.sum})
negativeTweets = dfSentiments.resample('30Min').agg({'negative': np.sum})
neutralTweets = dfSentiments.resample('30Min').agg({'neutral': np.sum})
plt.subplot(121)
labelsLine = ['total_tweets', 'neutral', 'positive', 'negative']
plt.plot(dfSentiments.resample('30Min').sum(), label=labelsLine)
plt.legend()
plt.title('Insights on with time')
# plt.show(dfSentiments.resample('H').sum().plot())


# Pie chart, where the slices will be ordered and plotted counter-clockwise:

plt.subplot(122)
labels = ['Positive', 'Negative', 'Neutral']
sizes = [sentiment_list["positive"], sentiment_list["negative"], sentiment_list["neutral"]]
colors = ['green', 'red', 'orange']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.savefig('PieGraph.png')  # Save it in a file
plt.show()                  # show it on IDE

