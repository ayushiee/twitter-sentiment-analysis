import json
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from TwitterApi.AuthenticationTokens import twitter_auth_tokens

consumer_key, consumer_key_secret, access_token, access_token_secret = twitter_auth_tokens.values()

class TwitterApiHelper(StreamListener):

    '''
    TwitterApiHelper:

    This class inherits StreamListener class from tweepy's streaming
    module to stream twitter tweets or get public tweets
    '''

    def __init__(self):
        # self.authentication = None
        self.authentication = OAuthHandler(
            consumer_key, consumer_key_secret)
        self.authentication.set_access_token(access_token, access_token_secret)

    def getPublicTweets(self, keyword):

        return tweepy.API(self.authentication).search(keyword)

    def startStreaming(self, keyword):
        """
        Starts the twitter streaming

        Params:
            self: self
        """

        # self.authentication = OAuthHandler(consumer_key, consumer_key_secret)
        # self.authentication.set_access_token(access_token, access_token_secret)

        Stream(self.authentication, self).filter(
            track=[keyword], is_async=True)

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
