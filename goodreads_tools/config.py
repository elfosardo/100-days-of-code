import configparser


API_URL = 'https://www.goodreads.com'

request_token_url = '{}/oauth/request_token'.format(API_URL)
authorize_url = '{}/oauth/authorize'.format(API_URL)
access_token_url = '{}/oauth/access_token'.format(API_URL)
auth_user_url = '{}/api/auth_user'.format(API_URL)
friend_list_url = '{}/friend/user'.format(API_URL)
shelves_list_url = '{}/shelf/list.xml'.format(API_URL)
followers_list_url = '{}/user/USER_ID/followers.xml'.format(API_URL)
following_list_url = '{}/user/USER_ID/following.xml'.format(API_URL)
books_owned_url = '{}/owned_books/user?format=xml&id=USER_ID'.format(API_URL)

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['DEFAULT']['GOODREADS_API_KEY']
api_secret = config['DEFAULT']['GOODREADS_API_SECRET']
user_email = config['DEFAULT']['USER_EMAIL']
