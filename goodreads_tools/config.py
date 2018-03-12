import configparser


API_URL = 'https://www.goodreads.com'

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['DEFAULT']['GOODREADS_API_KEY']
api_secret = config['DEFAULT']['GOODREADS_API_SECRET']
user_id = config['DEFAULT']['USER_ID']
