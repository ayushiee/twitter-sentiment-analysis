from tweepy.streaming import StreamListener
import json

class TwitterApiStream(StreamListener):

    '''
    TwitterApiStream:

    This class inherits StreamListener class from tweepy's streaming
    module to stream twitter tweets
    '''

    # def __init__(self):

    def set_auth_tokens(self, token):
        print(token)

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
