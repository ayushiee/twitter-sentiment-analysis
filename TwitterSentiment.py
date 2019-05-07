from textblob import TextBlob
from TwitterApi.TwitterApiHelper import TwitterApiHelper
from Model.SentimentAnalysis import SentimentAnalysis

keyword = input('Enter the Keyword: ')
twitterApiHelper = TwitterApiHelper()
publicTweets = twitterApiHelper.getPublicTweets(keyword=keyword)
model = SentimentAnalysis(publicTweets)
model.runSentimentAnalysis()
model.generateReport()

