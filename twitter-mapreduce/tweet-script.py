"""
Script to retrieve tweets via tweepy & the twitter api
Usage: Run ./get-tweets.py <hashtag word>
"""

#Import the necessary methods from tweepy library
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sys

#Variables that contains the user credentials to access Twitter API
consumer_key = 'Phwgk7y3GM3WoG60v9utSZEiR'
consumer_secret = '5qrMEcxXhbqjzw8ZeDCAZMwMGlqXCKqGE3eCBvCHMBleUagvO2'
access_token = '384061672-fJUvP0ldbgsI8BRCrseFuh95K9kGh5zs44AB1UPR'
access_token_secret = 'DHW9Oz2tHDaMo3tt2YJhw6fDaBEGf6b1cdaXtKHnWjUQ6'

hashtag_word = sys.argv[1]
if ('#' not in hashtag_word):
    hashtag_word = "#" + sys.argv[1]

#This is a basic listener that just prints received tweets to stdout.
class tweet_grab:

    def on_data(self, hashtag):
        count = 0
        # Copy from twitter to file
        with open('fetched_tweets.txt','a') as tf:
            for page in tweepy.Cursor(api.search, q=hashtag, rpp=100, result_type="recent").pages():
                for tweet in page:
                    # Exclude Retweets from tweets written to file
                    if (not tweet.retweeted) and ('RT @' not in tweet.text):
                        tf.write('\n\n\n')
                        tf.write(tweet.text)
                count+=1
                print("pages gathered so far: ", count)
            return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit_notify=True, wait_on_rate_limit=True)
    tweet_grab().on_data(hashtag_word)

    sys.exit
