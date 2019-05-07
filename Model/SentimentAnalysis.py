import time
from textblob import TextBlob
from termcolor import colored
import matplotlib.pyplot as plt


class SentimentAnalysis():
    '''
    SentimentAnalysis:

    Contains utility methods for sentiment analysis on twitter tweets
    '''

    def __init__(self, keyword, publicTweets):
        self.keyword = keyword
        self.publicTweets = publicTweets
        self.analysisResult = {
            'positive': 0,
            'negative': 0
        }

    def runSentimentAnalysis(self):
        print(colored('Retrieved Tweets Data', 'blue'))
        for tweet in self.publicTweets:
            originalTweet = tweet.text
            analysis = TextBlob(tweet.text)
            if analysis.sentiment[0] > 0:
                self.analysisResult['positive'] += 1
                print('-> ' + originalTweet + colored(' Positive', 'green'))
            else:
                self.analysisResult['negative'] += 1
                print('-> ' + originalTweet + colored(' Negative', 'red'))
            print('')

    def generateReport(self):

        print(colored('Analysis Reports Saved', 'green'))

        labels = ['Positive', 'Negative']
        values = [values for values in self.analysisResult.values()]

        plt.title('Analysis Report on: ' + self.keyword)
        plt.pie(values, labels=labels, autopct='%1.f%%')
        plt.savefig('./Reports/' + self.keyword +
                    '-' + int(time.time()) + '.png')
        plt.show()
