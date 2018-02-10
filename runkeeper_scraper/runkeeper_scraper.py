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


class RunkeeperUser:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.is_authenticated = False
        self.profile_name = self.get_profile_name()
        self.total_distance = self.get_total_distance()
        self.total_activities = self.get_total_activities()
        self.total_calories = self.get_total_calories()

    def authenticate(self):
        login_url = '{}/login'.format(SITE_URL)
        hidden_payload = self.get_hidden_payload(login_url)
        post = session.post(login_url, data=hidden_payload)
        cookie = post.cookies.get('checker')
        if not cookie:
            raise AuthenticationFailed('Cookie not generated. Wrong Password?')
        return True

    @staticmethod
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

    def get_profile_name(self):
        if not self.is_authenticated:
            self.authenticate()
        home_url = '{}/home'.format(SITE_URL)
        real_home = session.get(home_url)
        soup = BfS(real_home.text, 'html.parser')
        profile_href = soup.find('a', {'href': re.compile(PROFILE_REGEX)})
        profile_path = profile_href.attrs['href']
        profile_name = profile_path.split('/')[2]
        return profile_name

    def get_profile_info(self, info):
        request_url = '{}/user/{}/profile'.format(SITE_URL, self.profile_name)
        request = session.get(request_url)
        html_code = request.text
        soup = BfS(html_code, 'html.parser')
        profile_info = soup.find('div', {'id': info}).find('h1').text
        return profile_info

    def get_total_distance(self):
        distance = self.get_profile_info('totalDistance')
        return distance

    def get_total_activities(self):
        activities = self.get_profile_info('totalActivities')
        return activities

    def get_total_calories(self):
        calories = self.get_profile_info('totalCalories')
        return calories


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get info from runkeeper site')
    parser.add_argument('email', metavar='email',
                        help='the username is your e-mail address')
    args = parser.parse_args()

    my_password = getpass.getpass()

    with requests.Session() as session:
        my_user = RunkeeperUser(args.email, my_password)

        print('User Profile: {}'.format(my_user.profile_name))
        print('Total Distance: {}'.format(my_user.total_distance))
        print('Total Activities: {}'.format(my_user.total_activities))
        print('Total Calories: {}'.format(my_user.total_calories))
