import json
import tweepy
import re
import os
import nltk
nltk.download('punkt')
nltk.download('stopwords')

from nltk.corpus import stopwords

from tweepy import OAuthHandler

consumer_key = os.environ["CONSUMER_KEY_API"]

consumer_secret = os.getenv("CONSUMER_SECRET_API")

access_token = os.getenv("ACCESS_TOKEN_API")

access_secret = os.getenv("ACCESS_SECRET_API")


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# we use 1 to limit the number of tweets we are reading
# and we only access the `text` of the tweet
print("*** We are printing here 1 tweet in text format from user's home timeline ***")
for status in tweepy.Cursor(api.home_timeline).items(1):
    print(status.text)

# Tweets that the user can see on his Homepage.  These are the tweets by the accounts you are following.
print("*** We are printing here 10 tweets in JSON format from user's home timeline ***")
for status in tweepy.Cursor(api.home_timeline).items(10):
    print(json.dumps(status._json, indent=2))

print("*** We are printing here 10 friends of the user in JSON format ***")
for friend in tweepy.Cursor(api.friends).items(10):
    print(json.dumps(friend._json, indent=2))

# Tweets that the user does itself
print("*** We are printing here 5 tweets that user did himself/herself, in JSON format ***")
for tweet in tweepy.Cursor(api.user_timeline).items(5):
    print(json.dumps(tweet._json, indent=2))

emoticons_str = r"""
    (?:
        [<>]?
        [:;=8]                          # eyes
        [\-o\*\'-]?                     # optional nose
        [\)\]\(\[dDpP/\:\>\<\}\{@\|\\]  # mouth
        |
        [\)\]\(\[dDpP/\:\>\<\}\{@\|\\]  # mouth
        [\-o\*\'-]?                     # optional nose
        [:;=8]                          # eyes
        [<>]?
        |
        <3                              # heart
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>',  # HTML tags
    r'[\w\.-]+@[\w\.-]+', # Email address
    r'(?:@[\w_]+)',  # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs

    r"\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}", # Phone number in formats
    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '

    r'(?:[\w_]+)',  # other words
    r'(?:\S)',  # anything else
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
tweets = tweepy.Cursor(api.home_timeline).items(15)

# Filter the tweets of English Language only and remove English stopwords
print("*** We are printing below the tokens of each of the latest 15 tweets from user's home "
      "if they are in English and also we remove the English stopwords. ***")

for tweet in tweets:
    if tweet.lang == "en":
        sw = stopwords.words('english')
        filtered = [w for w in preprocess(tweet.text) if not w in sw]
        print(filtered)

# Tweet used just to check for email and phone number validity.
print("*** We are printing below a sample tweet to check for email and phone number validity. ***")
Mytweet = 'RT @JordiTorresBCN: just an example! :D http://JordiTorres.Barcelona #masterMEI, ' \
          'Call at 123-444-5678 or email: urdu@mydomian.pa'
sw = stopwords.words('english')
MyFilteredTweet = [w for w in preprocess(Mytweet) if not w in sw]
print(MyFilteredTweet)
