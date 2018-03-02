import json
import tweepy
from tweepy import OAuthHandler

consumer_key = '1deFGmrbgFbStqyL8cVpPzIxF'
consumer_secret = 'n1JkNlPU0cvE7KSeAie5oVKS0DPKFwkbj0uR0QmcgfxNdhiF5H'
access_token = '1970784110-tVo2cCOU4QZ2jgZ7eVM5vx2ecZB1uTgQD49bigY'
access_secret = 'aMpny0PzDyLFcc5vV7nim8G0CgkefLMLCjtSFJ0KJ3m2p'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# we use 1 to limit the number of tweets we are reading
# and we only access the `text` of the tweet
for status in tweepy.Cursor(api.home_timeline).items(1):
    print(status.text)

# Tweets that the user can see on his Homepage. This are done by the accounts you are following.
for status in tweepy.Cursor(api.home_timeline).items(10):
    print(json.dumps(status._json, indent=2))

for friend in tweepy.Cursor(api.friends).items(15):
    print(json.dumps(friend._json, indent=2))

# Tweets that the user does itself
for tweet in tweepy.Cursor(api.user_timeline).items(5):
    print(json.dumps(tweet._json, indent=2))
