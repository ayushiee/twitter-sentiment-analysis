from textblob import TextBlob
from termcolor import colored
from TwitterApi.TwitterApiHelper import TwitterApiHelper
from Model.SentimentAnalysis import SentimentAnalysis

keyword = input(colored('[?] Enter the Keyword: ', 'blue'))
twitterApiHelper = TwitterApiHelper()
publicTweets = twitterApiHelper.getPublicTweets(keyword=keyword)
model = SentimentAnalysis(keyword, publicTweets)
model.runSentimentAnalysis()
model.generateReport()

