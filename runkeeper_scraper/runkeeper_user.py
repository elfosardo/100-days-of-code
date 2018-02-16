import config
import json
import re
import runkeeper_errors as rke
from bs4 import BeautifulSoup as BfS


class RunkeeperUser:
    def __init__(self, email, password, session):
        self.email = email
        self.password = password
        self.session = session
        self.is_authenticated = False
        self.profile_name = self.get_profile_name()
        self.total_distance = self.get_total_distance()
        self.total_activities = self.get_total_activities()
        self.total_calories = self.get_total_calories()

    def authenticate(self):
        login_url = '{}/login'.format(config.SITE_URL)
        hidden_payload = self.get_hidden_payload(login_url)
        post = self.session.post(login_url, data=hidden_payload)
        cookie = post.cookies.get('checker')
        if not cookie:
            raise rke.AuthenticationFailed('Cookie not generated. Wrong Password?')
        return True

    def get_hidden_payload(self, login_url):
        login_page = self.session.get(login_url)
        my_soup = BfS(login_page.text, 'html.parser')
        login_form = my_soup.find_all('input', {'type': 'hidden'})
        hidden_payload = {}
        for element in login_form:
            hidden_payload[element.attrs['name']] = element.attrs['value']
        hidden_payload['email'] = self.email
        hidden_payload['password'] = self.password
        return hidden_payload

    def get_profile_name(self):
        if not self.is_authenticated:
            self.authenticate()
        home_url = '{}/home'.format(config.SITE_URL)
        real_home = self.session.get(home_url)
        soup = BfS(real_home.text, 'html.parser')
        profile_href = soup.find('a', {'href': re.compile(config.PROFILE_REGEX)})
        profile_path = profile_href.attrs['href']
        profile_name = profile_path.split('/')[2]
        return profile_name

    def get_profile_info(self, info):
        request_url = '{}/user/{}/profile'.format(config.SITE_URL, self.profile_name)
        request = self.session.get(request_url)
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

    def get_activities_by_month_year(self, month, year):
        start_date = "{}-01-{}".format(month, year)
        payload = {"userName": self.profile_name, "startDate": start_date}
        url = "{}/activitiesByDateRange".format(config.SITE_URL)
        request = self.session.get(url, params=payload)
        activities_in_month = json.loads(request.text)['activities']
        return activities_in_month
