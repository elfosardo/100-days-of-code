import configparser


API_URL = 'https://www.goodreads.com'

request_token_url = '{}/oauth/request_token'.format(API_URL)
authorize_url = '{}/oauth/authorize'.format(API_URL)
access_token_url = '{}/oauth/access_token'.format(API_URL)
auth_user_url = '{}/api/auth_user'.format(API_URL)

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['DEFAULT']['GOODREADS_API_KEY']
api_secret = config['DEFAULT']['GOODREADS_API_SECRET']
user_email = config['DEFAULT']['USER_EMAIL']
