import configparser


SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = '587'

config = configparser.ConfigParser()
config.read('config.ini')

gmail_app_pw = config['DEFAULT']['GMAIL_APP_PW']
