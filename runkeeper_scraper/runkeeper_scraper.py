import argparse
import getpass
import requests
import re
from bs4 import BeautifulSoup as BS


SITE_URL = 'https://runkeeper.com'
LOGIN_URL = 'https://runkeeper.com/login'


def get_profile_name():
    my_home = '{}/home'.format(SITE_URL)
    print(my_home)
    real_home = session.get(my_home)
    soup = BS(real_home.text, 'html.parser')
    profile_link = soup.find('a', {'href': re.compile(r"/user/[a-zA-Z0-9]*/profile")})
#    profile_urlo = profile_link.text
#    profile_name =
    return profile_link


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get info from runkeeper site')
    parser.add_argument('email', metavar='email',
                        help='the username is your e-mail address')
    parser.add_argument('profile_name', metavar='Profile Name',
                        help='Name of the profile')
    args = parser.parse_args()

    my_password = getpass.getpass()

    request_url = "https://runkeeper.com/user/{}/profile".format(args.profile_name)

    print(request_url)

#    payload = {
#        'email': args.email,
#        'password': my_password
#    }

    with requests.Session() as session:

        login_page = session.get(LOGIN_URL)
        my_soup = BS(login_page.text, 'html.parser')
        login_form = my_soup.find_all('input', {'type': 'hidden'})
        hidden_payload = {}
        for element in login_form:
            hidden_payload[element.attrs['name']] = element.attrs['value']
        hidden_payload['email'] = args.email
        hidden_payload['password'] = my_password
        #print(hidden_payload)
        post = session.post(LOGIN_URL, data=hidden_payload)
        cookie = post.cookies.get('checker')
        print(cookie)
        r = session.get(request_url)
        #print(r.text)
        html_code = r.text
        my_soup = BS(html_code, 'html.parser')
        #print(my_soup.prettify())
        total_activities = my_soup.find('div', {'id': 'totalActivities'}).find('h1')
        print(total_activities.text)

        profile_url = get_profile_name()
        print(profile_url)


