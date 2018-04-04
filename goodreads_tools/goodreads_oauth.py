import oauth2
import config as cfg
import getpass
import time
import xml
import urllib.parse as up

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from goodreads_book import GoodreadsBook


def get_client():
    token_key = cfg.config['SECRETS']['TOKEN_KEY']
    token_secret = cfg.config['SECRETS']['TOKEN_SECRET']
    token = oauth2.Token(token_key, token_secret)
    consumer = oauth2.Consumer(key=cfg.api_key,
                               secret=cfg.api_secret)
    client = oauth2.Client(consumer, token)
    return client


def get_content(client, request_url, req_type):
    response, content = client.request(request_url, req_type)
    if response['status'] != '200':
        raise Exception('Invalid response: {} {}, content: '
                        .format(response['status'], content))
    return content


def get_user_id():
    client = get_client()
    content = get_content(client=client,
                          request_url=cfg.auth_user_url,
                          req_type='GET')
    userxml = xml.dom.minidom.parseString(content)
    user_id = userxml.getElementsByTagName('user')[0].attributes['id'].value
    return str(user_id)


def save_user_id():
    user_id = get_user_id()
    new_config_values = {'USER_ID': user_id}
    update_config_file(section='DEFAULT',
                       new_values=new_config_values)
    return 'user_id saved in configuration file'


def clear_and_fill_element(driver, element_id, value):
    element = driver.find_element_by_id(element_id)
    element.clear()
    element.send_keys(value)
    return 'element filled'


def authorize_token(authorize_link, password):
    driver = webdriver.Firefox()
    driver.get(authorize_link)
    assert 'Sign in' in driver.title
    clear_and_fill_element(driver=driver, element_id='user_email',
                           value=cfg.user_email)
    clear_and_fill_element(driver=driver, element_id='user_password',
                           value=password)
    remember_me_elem = driver.find_element_by_id('remember_me')
    remember_me_elem.click()
    driver.find_element_by_name('next').click()
    try:
        driver.find_element_by_xpath("//input[@name='commit'"
                                     "and @value='Allow access']").click()
    except NoSuchElementException:
        time.sleep(2)
    driver.close()
    return 'token authorized'


def update_config_file(section, new_values):
    for k, v in new_values.items():
        cfg.config[section][k] = v
    try:
        with open('config.ini', 'w') as config_file:
            cfg.config.write(config_file)
    except IOError:
        print('cannot open file {}'.format(config_file))
    config_file.close()
    return 'config file updated'


def get_token_values():
    consumer = oauth2.Consumer(key=cfg.api_key,
                               secret=cfg.api_secret)

    client = oauth2.Client(consumer)

    content = get_content(client=client,
                          request_url=cfg.request_token_url,
                          req_type='GET')

    request_token = dict(up.parse_qsl(content.decode('utf-8')))

    authorize_link = '{}?oauth_token={}'.format(cfg.authorize_url,
                                                request_token['oauth_token'])

    print('Authorizing token using Selenium driver')
    my_password = getpass.getpass('Goodreads Password: ')

    authorize_token(authorize_link=authorize_link,
                    password=my_password)

    token = oauth2.Token(request_token['oauth_token'],
                         request_token['oauth_token_secret'])

    client = oauth2.Client(consumer, token)

    content = get_content(client=client,
                          request_url=cfg.access_token_url,
                          req_type='POST')

    access_token = dict(up.parse_qsl(content.decode('utf-8')))
    token_key = access_token['oauth_token']
    token_secret = access_token['oauth_token_secret']

    return token_key, token_secret


def save_token_values():
    token_key, token_secret = get_token_values()
    print('Saving OAuth token codes in config file')
    new_config_values = {'TOKEN_KEY': token_key,
                         'TOKEN_SECRET': token_secret}
    update_config_file(section='SECRETS',
                       new_values=new_config_values)
    return 'OAuth token codes saved in configuration file'


def get_xml_content(request_url, request_type):
    client = get_client()
    xml_content = get_content(client=client,
                              request_url=request_url,
                              req_type=request_type)
    return xml_content


def get_friends_list(user_id):
    friends_list_url = '{}/{}?format=xml'.format(cfg.friend_list_url, user_id)
    friends_list = generate_info_list(friends_list_url)
    return friends_list


def get_following_list(user_id):
    following_list_url = cfg.following_list_url.replace('USER_ID', user_id)
    following_list = generate_info_list(following_list_url)
    return following_list


def get_followers_list(user_id):
    followers_list_url = cfg.followers_list_url.replace('USER_ID', user_id)
    followers_list = generate_info_list(followers_list_url)
    return followers_list


def get_books_owned(user_id):
    books_owned = []
    books_owned_url = cfg.books_owned_url.replace('USER_ID', user_id)
    xml_content = get_xml_content(request_url=books_owned_url,
                                  request_type='GET')
    content = xml.dom.minidom.parseString(xml_content)
    dom_list = content.getElementsByTagName('owned_book')
    for element in dom_list:
        book_elem_xml = element.getElementsByTagName('book')[0]
        book_title_xml = book_elem_xml.getElementsByTagName('title')[0]
        book_title = book_title_xml.firstChild.nodeValue
        book_id_xml = book_elem_xml.getElementsByTagName('id')[0]
        book_id = book_id_xml.firstChild.nodeValue
        book = GoodreadsBook(book_id=book_id,
                             book_title=book_title)
        books_owned.append(book)
    return books_owned


def generate_info_list(list_url):
    info_list = []
    xml_content = get_xml_content(request_url=list_url,
                                  request_type='GET')
    content = xml.dom.minidom.parseString(xml_content)
    dom_list = content.getElementsByTagName('user')
    for element in dom_list[1:]:
        name_elem = element.getElementsByTagName('name')[0]
        name = name_elem.firstChild.nodeValue
        info_list.append(name)
    return info_list
