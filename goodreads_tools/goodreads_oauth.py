import oauth2
import config as cfg
import getpass
import time
import xml
import urllib.parse as up

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def get_content(client, request_url, req_type):
    response, content = client.request(request_url, req_type)
    if response['status'] != '200':
        raise Exception('Invalid response: {} {}, content: '.format(response['status'],
                                                                    content))
    return content


def get_user_id(content):
    userxml = xml.dom.minidom.parseString(content)
    user_id = userxml.getElementsByTagName('user')[0].attributes['id'].value
    return str(user_id)


def clear_and_fill_element(driver, element_id, value):
    element = driver.find_element_by_id(element_id)
    element.clear()
    element.send_keys(value)


def authorize_token():
    driver = webdriver.Firefox()
    driver.get(authorize_link)
    assert 'Sign in' in driver.title
    clear_and_fill_element(driver=driver, element_id='user_email', value=cfg.user_email)
    clear_and_fill_element(driver=driver, element_id='user_password', value=my_password)
    remember_me_elem = driver.find_element_by_id('remember_me')
    remember_me_elem.click()
    driver.find_element_by_name('next').click()
    try:
        driver.find_element_by_xpath("//input[@name='commit' and @value='Allow access']").click()
    except NoSuchElementException:
        time.sleep(2)
    driver.close()


def update_config_file(section, new_values):
    for k, v in new_values.items():
        cfg.config[section][k] = v
    try:
        with open('config.ini', 'w') as config_file:
            cfg.config.write(config_file)
    except IOError:
        print('cannot open file {}'.format(config_file))
    config_file.close()


if __name__ == '__main__':
    url = cfg.API_URL
    request_token_url = '{}/oauth/request_token'.format(url)
    authorize_url = '{}/oauth/authorize'.format(url)
    access_token_url = '{}/oauth/access_token'.format(url)
    auth_user_url = '{}/api/auth_user'.format(url)

    consumer = oauth2.Consumer(key=cfg.api_key,
                               secret=cfg.api_secret)

    client = oauth2.Client(consumer)

    content = get_content(client=client,
                          request_url=request_token_url,
                          req_type='GET')

    request_token = dict(up.parse_qsl(content.decode('utf-8')))

    authorize_link = '{}?oauth_token={}'.format(authorize_url,
                                                request_token['oauth_token'])
    print('Authorizing token using Selenium driver')
    my_password = getpass.getpass('Goodreads Password: ')

    authorize_token()

    token = oauth2.Token(request_token['oauth_token'],
                         request_token['oauth_token_secret'])

    client = oauth2.Client(consumer, token)

    content = get_content(client=client,
                          request_url=access_token_url,
                          req_type='POST')

    access_token = dict(up.parse_qsl(content.decode('utf-8')))
    token_key = access_token['oauth_token']
    token_secret = access_token['oauth_token_secret']

    print('Saving OAuth token codes in config file')

    new_config_values = {'TOKEN_KEY': token_key,
                         'TOKEN_SECRET': token_secret}

    update_config_file(section='SECRETS',
                       new_values=new_config_values)

    print('OAuth token codes saved!')

    # Testing new config values
    token_key = cfg.config['SECRETS']['TOKEN_KEY']
    token_secret = cfg.config['SECRETS']['TOKEN_SECRET']
    token = oauth2.Token(token_key, token_secret)
    client = oauth2.Client(consumer, token)
    content = get_content(client=client,
                          request_url=auth_user_url,
                          req_type='GET')
    user_id = get_user_id(content)
    print('My user id: {}'.format(user_id))
