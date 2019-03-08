from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

# Authentication Key's for Twitter API
consumer_key = '[consumer_key]'
consumer_key_secret = '[consumer_key_secret]'
access_token = '[access_token]'
access_token_secret = '[access_token_secret]'

'''

'''
class Listener(StreamListener):

    def on_data(self, data):

	    all_data = json.loads(data)
	    tweet = all_data['text']
		# sentiment_value, confidence = s.sentiment(tweet)
		# print(tweet, sentiment_value, confidence)

		# if confidence*100 >= 80:
		# 	output = open('twitter-out.txt','a')
		# 	output.write(sentiment_value)
		# 	output.write('\n')
		# 	output.close()

    def on_error(self, status):
        print(status)

auth = OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)

twitterStream = Stream(auth, Listener())
twitterStream.filter(track=["happy"])
