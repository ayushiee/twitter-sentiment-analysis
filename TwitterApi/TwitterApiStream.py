import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from TwitterApi.AuthenticationTokens import twitter_auth_tokens


consumer_key, consumer_key_secret, access_token, access_token_secret = twitter_auth_tokens.values()


class TwitterApiStream(StreamListener):

    '''
    TwitterApiStream:

    This class inherits StreamListener class from tweepy's streaming
    module to stream twitter tweets
    '''

    def __init__(self):
        self.authentication = None

    def startStreaming(self):
        """
        Starts the twitter streaming

        Params:
            self: self
        """

        self.authentication = OAuthHandler(consumer_key, consumer_key_secret)
        self.authentication.set_access_token(access_token, access_token_secret)

        Stream(self.authentication, self).filter(
            track=['donald trump'], is_async=True)

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
