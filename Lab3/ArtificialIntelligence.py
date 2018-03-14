import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener


class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('ArtificialIntelligenceTweets.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True


consumer_key = os.environ["CONSUMER_KEY_API"]
consumer_secret = os.getenv("CONSUMER_SECRET_API")
access_token = os.getenv("ACCESS_TOKEN_API")
access_secret = os.getenv("ACCESS_SECRET_API")

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['ArtificialIntelligence'])
