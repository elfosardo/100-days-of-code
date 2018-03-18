import oauth2
import config as cfg
import getpass
import time
import urllib.parse as up

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def get_content(client, token_url, req_type):
    response, content = client.request(token_url, req_type)
    if response['status'] != '200':
        raise Exception('Invalid response: {} {}, content: '.format(response['status'],
                                                                    content))
    return content


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


if __name__ == '__main__':
    url = cfg.API_URL
    request_token_url = '{}/oauth/request_token'.format(url)
    authorize_url = '{}/oauth/authorize'.format(url)
    access_token_url = '{}/oauth/access_token'.format(url)

    consumer = oauth2.Consumer(key=cfg.api_key,
                               secret=cfg.api_secret)

    client = oauth2.Client(consumer)

    content = get_content(client=client,
                          token_url=request_token_url,
                          req_type='GET')

    request_token = dict(up.parse_qsl(content.decode('utf-8')))

    authorize_link = '{}?oauth_token={}'.format(authorize_url,
                                                request_token['oauth_token'])
    print('Authorizing token using Selenium driver')
    print(authorize_link)
    my_password = getpass.getpass('Goodreads Password: ')

    authorize_token()

    token = oauth2.Token(request_token['oauth_token'],
                         request_token['oauth_token_secret'])

    client = oauth2.Client(consumer, token)

    content = get_content(client=client,
                          token_url=access_token_url,
                          req_type='POST')

    access_token = dict(up.parse_qsl(content.decode('utf-8')))
    token_key = access_token['oauth_token']
    token_secret = access_token['oauth_token_secret']

    print('OAuth token codes')
    print('oauth token key:    {}'.format(token_key))
    print('oauth token secret: {}'.format(token_secret))

    token = oauth2.Token(token_key, token_secret)
    print(token)
