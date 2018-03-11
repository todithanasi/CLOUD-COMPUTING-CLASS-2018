import tweepy
import os
from tweepy import OAuthHandler

consumer_key = os.environ["CONSUMER_KEY_API"]

consumer_secret = os.getenv("CONSUMER_SECRET_API")

access_token = os.getenv("ACCESS_TOKEN_API")

access_secret = os.getenv("ACCESS_SECRET_API")

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
user = api.me()

print('Name: ' + user.name)
print('Location: ' + user.location)
print('Friends: ' + str(user.followers_count))
print('Created: ' + str(user.created_at))
print('Description: ' + str(user.description))
