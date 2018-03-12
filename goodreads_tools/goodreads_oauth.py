import oauth2
import config as cfg
import urllib.parse as up

url = cfg.API_URL
request_token_url = '{}/oauth/request_token'.format(url)
authorize_url = '{}/oauth/authorize'.format(url)
access_token_url = '{}/oauth/access_token'.format(url)

consumer = oauth2.Consumer(key=cfg.api_key,
                           secret=cfg.api_secret)

client = oauth2.Client(consumer)

response, content = client.request(request_token_url, 'GET')
if response['status'] != '200':
    raise Exception('Invalid response: {}, content: '.format(response['status'] + content))

request_token = dict(up.parse_qsl(content.decode('utf-8')))

authorize_link = '{}?oauth_token={}'.format(authorize_url, request_token['oauth_token'])
print('Use a browser to visit this link and accept your application:')
print(authorize_link)
