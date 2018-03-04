import configparser


API_URL = 'https://openexchangerates.org/api'

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['DEFAULT']['OPEN_EXCHANGE_APP_ID']
