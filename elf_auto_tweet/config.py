import configparser
import tweepy

config = configparser.ConfigParser()
config.read('config.ini')

consumer_key = config['DEFAULT']['CONSUMER_KEY']
consumer_secret = config['DEFAULT']['CONSUMER_SECRET']
access_token = config['DEFAULT']['ACCESS_TOKEN']
access_token_secret = config['DEFAULT']['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
