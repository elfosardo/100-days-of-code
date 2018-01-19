import configparser
import logging
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

logging.basicConfig(level=logging.DEBUG,
                    datefmt='%y-%m-%d %H:%M:%S',
                    filename='elf_auto_tweet.log',
                    format='%(asctime)s %(name)s-10s %(levelname)-8s %(message)s')
