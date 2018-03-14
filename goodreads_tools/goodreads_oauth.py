import oauth2
import config as cfg
import getpass
import urllib.parse as up

from selenium import webdriver


def authorize_token():
    driver = webdriver.Firefox()
    driver.get(authorize_link)
    assert 'Sign in' in driver.title
    username_elem = driver.find_element_by_id('user_email')
    username_elem.clear()
    username_elem.send_keys(cfg.user_email)
    password_elem = driver.find_element_by_id('user_password')
    password_elem.clear()
    password_elem.send_keys(my_password)
    remember_me_elem = driver.find_element_by_id('remember_me')
    remember_me_elem.click()
    driver.find_element_by_name('next').click()
    driver.find_element_by_xpath("//input[@name='commit' and @value='Allow access']").click()


if __name__ == '__main__':
    url = cfg.API_URL
    request_token_url = '{}/oauth/request_token'.format(url)
    authorize_url = '{}/oauth/authorize'.format(url)
    access_token_url = '{}/oauth/access_token'.format(url)

    consumer = oauth2.Consumer(key=cfg.api_key,
                               secret=cfg.api_secret)

    client = oauth2.Client(consumer)

    response, content = client.request(request_token_url, 'GET')
    if response['status'] != '200':
        raise Exception('Invalid response: {} {}, content: '.format(response['status'], content))

    request_token = dict(up.parse_qsl(content.decode('utf-8')))

    authorize_link = '{}?oauth_token={}'.format(authorize_url, request_token['oauth_token'])
    print('Authorizing token using Selenium driver')
    print(authorize_link)
    my_password = getpass.getpass('Goodreads Password: ')

    authorize_token()
