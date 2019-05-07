from textblob import TextBlob
from TwitterApi.TwitterApiHelper import TwitterApiHelper

publicTweets = TwitterApiHelper().getPublicTweets(keyword='trump')

for tweet in publicTweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	if analysis.sentiment[0] > 0:
		print('Positive')
	else:
		print('Negative')
	print('')

