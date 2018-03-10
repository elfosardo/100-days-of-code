import configparser


API_URL = 'https://www.goodreads.com'

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['DEFAULT']['GOODREADS_API_KEY']
user_id = config['DEFAULT']['USER_ID']
