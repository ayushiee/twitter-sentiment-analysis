from tweepy import Stream
from tweepy import OAuthHandler

from TwitterApi.TwitterApiStream import TwitterApiStream
from keys.twitter import twitter_auth

consumer_key, consumer_key_secret, access_token, access_token_secret = twitter_auth.values()


auth = OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)

twitterStream = Stream(auth, TwitterApiStream())
twitterStream.filter(track=['donald trump'])
