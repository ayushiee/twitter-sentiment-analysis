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
        """
        Retrieves the latest public tweets from the twitter with a
        particular keyword

        Params:
            self: Object
            keyword: String

        returns:
           public tweets data
        """

        return tweepy.API(self.authentication).search(keyword)

    def startStreaming(self, keyword):
        """
        Starts the twitter streaming in async mode

        Params:
            self: Object
            keyword: String
        """

        Stream(self.authentication, self).filter(
            track=[keyword], is_async=True)

    def on_data(self, data):
        """
        Invoked on data stream success

        Params:
            self: Object
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
