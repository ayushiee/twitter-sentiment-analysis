from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

# Authentication Key's for Twitter API
from keys.twitter import twitter_auth

consumer_key, consumer_key_secret, access_token, access_token_secret = twitter_auth.values()


class TwitterStream(StreamListener):

    '''
    TwitterStream:

    This class inherits StreamListener class from tweepy's streaming
    module to stream twitter tweets
    '''

    def on_data(self, data):
        """
        Invoked on data stream success

        Params:
            self: self
            data: json response
        """   
        parsed_data = json.loads(data)
        tweet = parsed_data['text']
        print(tweet)

    def on_error(self, status):
        """
        Invoked on data stream error

        Params:
            self: self
            data: status
        """
        print(status)


auth = OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)

twitterStream = Stream(auth, TwitterStream())
twitterStream.filter(track=['donald trump'])
