import argparse
import getpass
import requests
import re
from bs4 import BeautifulSoup as BfS


SITE_URL = 'https://runkeeper.com'
PROFILE_REGEX = r"/user/[a-zA-Z0-9]*/profile"


class Error(Exception):
    pass


class AuthenticationFailed(Error):
    def __init__(self, message):
        self.message = message


def authenticate():
    login_url = '{}/login'.format(SITE_URL)
    hidden_payload = get_hidden_payload(login_url)
    post = session.post(login_url, data=hidden_payload)
    cookie = post.cookies.get('checker')
    if not cookie:
        raise AuthenticationFailed('Cookie not generated. Wrong Password?')
    return True


def get_hidden_payload(login_url):
    login_page = session.get(login_url)
    my_soup = BfS(login_page.text, 'html.parser')
    login_form = my_soup.find_all('input', {'type': 'hidden'})
    hidden_payload = {}
    for element in login_form:
        hidden_payload[element.attrs['name']] = element.attrs['value']
    hidden_payload['email'] = args.email
    hidden_payload['password'] = my_password
    return hidden_payload


def get_profile_name():
    home_url = '{}/home'.format(SITE_URL)
    real_home = session.get(home_url)
    soup = BfS(real_home.text, 'html.parser')
    profile_href = soup.find('a', {'href': re.compile(PROFILE_REGEX)})
    profile_path = profile_href.attrs['href']
    profile_name = profile_path.split('/')[2]
    return profile_name


def get_profile_soup():
    my_profile_name = get_profile_name()
    request_url = '{}/user/{}/profile'.format(SITE_URL, my_profile_name)
    request = session.get(request_url)
    html_code = request.text
    soup = BfS(html_code, 'html.parser')
    return soup


def get_total_kms():
    kms = my_profile_soup.find('div', {'id': 'totalDistance'}).find('h1')
    return kms


def get_total_activities():
    activities = my_profile_soup.find('div', {'id': 'totalActivities'}).find('h1')
    return activities


def get_total_calories():
    calories = my_profile_soup.find('div', {'id': 'totalCalories'}).find('h1')
    return calories


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get info from runkeeper site')
    parser.add_argument('email', metavar='email',
                        help='the username is your e-mail address')
    args = parser.parse_args()

    my_password = getpass.getpass()

    with requests.Session() as session:
        authenticate()
        my_profile_soup = get_profile_soup()
        total_kms = get_total_kms().text
        total_activities = get_total_activities().text
        total_calories = get_total_calories().text

        print('Total km: {}'.format(total_kms))
        print('Total Activities: {}'.format(total_activities))
        print('Total Calories: {}'.format(total_calories))
