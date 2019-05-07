from textblob import TextBlob
from Utils.ConsoleUtils import ConsoleUtils
from termcolor import colored


class SentimentAnalysis():

    def __init__(self, publicTweets):
        self.publicTweets = publicTweets

    def runSentimentAnalysis(self):

        for tweet in self.publicTweets:
            originalTweet = tweet.text
            analysis = TextBlob(tweet.text)
            if analysis.sentiment[0] > 0:
                print(originalTweet + colored(' Positive', 'green'))
            else:
                print(originalTweet + colored(' Negative', 'red'))
            print('')

    def generateReport(self):

        print('generating report')
