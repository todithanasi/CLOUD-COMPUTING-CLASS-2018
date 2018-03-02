import tweepy
from tweepy import OAuthHandler

consumer_key = '1deFGmrbgFbStqyL8cVpPzIxF'
consumer_secret = 'n1JkNlPU0cvE7KSeAie5oVKS0DPKFwkbj0uR0QmcgfxNdhiF5H'
access_token = '1970784110-tVo2cCOU4QZ2jgZ7eVM5vx2ecZB1uTgQD49bigY'
access_secret = 'aMpny0PzDyLFcc5vV7nim8G0CgkefLMLCjtSFJ0KJ3m2p'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
user = api.me()

print('Name: ' + user.name)
print('Location: ' + user.location)
print('Friends: ' + str(user.followers_count))
print('Created: ' + str(user.created_at))
print('Description: ' + str(user.description))
