import json
import tweepy
import re

from tweepy import OAuthHandler

consumer_key = '1deFGmrbgFbStqyL8cVpPzIxF'
consumer_secret = 'n1JkNlPU0cvE7KSeAie5oVKS0DPKFwkbj0uR0QmcgfxNdhiF5H'
access_token = '1970784110-tVo2cCOU4QZ2jgZ7eVM5vx2ecZB1uTgQD49bigY'
access_secret = 'aMpny0PzDyLFcc5vV7nim8G0CgkefLMLCjtSFJ0KJ3m2p'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# # we use 1 to limit the number of tweets we are reading
# # and we only access the `text` of the tweet
# for status in tweepy.Cursor(api.home_timeline).items(1):
#     print(status.text)

# Tweets that the user can see on his Homepage.  These are the tweets by the accounts you are following.
# for status in tweepy.Cursor(api.home_timeline).items(10):
#     print(json.dumps(status._json, indent=2))

# for friend in tweepy.Cursor(api.friends).items(15):
#     print(json.dumps(friend._json, indent=2))
#
# # Tweets that the user does itself
# for tweet in tweepy.Cursor(api.user_timeline).items(5):
#     print(json.dumps(tweet._json, indent=2))

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>',  # HTML tags
    r'(?:@[\w_]+)',  # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs

    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
    r'(?:[\w_]+)',  # other words
    r'(?:\S)'  # anything else
]

tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)


def tokenize(s):
    return tokens_re.findall(s)


def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens


# Take Tweets that the user can see on his Homepage. (These are the tweets by the accounts you are following).
tweets = tweepy.Cursor(api.home_timeline).items(10)

# Filter the tweets of English Language only
for tweet in tweets:
    if tweet.lang == "en":
        print(preprocess(tweet.text))
