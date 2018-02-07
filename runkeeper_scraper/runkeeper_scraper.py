import argparse
import getpass
import requests
import re
from bs4 import BeautifulSoup as BfS


SITE_URL = 'https://runkeeper.com'
LOGIN_URL = 'https://runkeeper.com/login'


def get_profile_name():
    my_home = '{}/home'.format(SITE_URL)
    real_home = session.get(my_home)
    soup = BfS(real_home.text, 'html.parser')
    profile_href = soup.find('a', {'href': re.compile(r"/user/[a-zA-Z0-9]*/profile")})
    profile_path = profile_href.attrs['href']
    profile_name = profile_path.split('/')[2]
    return profile_name


def get_total_activities():
    request_url = "{}/user/{}/profile".format(SITE_URL, my_profile_name)
    request = session.get(request_url)
    html_code = request.text
    soup = BfS(html_code, 'html.parser')
    activities = soup.find('div', {'id': 'totalActivities'}).find('h1')
    return activities


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get info from runkeeper site')
    parser.add_argument('email', metavar='email',
                        help='the username is your e-mail address')
    args = parser.parse_args()

    my_password = getpass.getpass()

    with requests.Session() as session:

        login_page = session.get(LOGIN_URL)
        my_soup = BfS(login_page.text, 'html.parser')
        login_form = my_soup.find_all('input', {'type': 'hidden'})
        hidden_payload = {}
        for element in login_form:
            hidden_payload[element.attrs['name']] = element.attrs['value']
        hidden_payload['email'] = args.email
        hidden_payload['password'] = my_password
        post = session.post(LOGIN_URL, data=hidden_payload)
        cookie = post.cookies.get('checker')

        my_profile_name = get_profile_name()

        total_activities = get_total_activities()

        print(total_activities.text)
