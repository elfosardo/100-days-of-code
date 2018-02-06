import argparse
import getpass
import requests
from bs4 import BeautifulSoup

LOGIN_URL = 'https://runkeeper.com/login'

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
        my_soup = BeautifulSoup(login_page.text, 'html.parser')
        login_form = my_soup.find_all('input', {'type': 'hidden'})
        hidden_payload = {}
        for element in login_form:
            hidden_payload[element.attrs['name']] = element.attrs['value']
        hidden_payload['email'] = args.email
        hidden_payload['password'] = my_password
        print(hidden_payload)
#        post = session.post(LOGIN_URL, data=payload)
#        cookie = post.cookies.get('checker')
#        print(cookie)
#        r = session.get(REQUEST_URL)
#        print(r.text)
#        html_code = urlopen(REQUEST_URL)
#        my_soup = BeautifulSoup(html_code, 'html.parser')
#        print(my_soup.prettify())
#        total_activities = my_soup.find('div', {'id': 'totalActivities'}).find_all('h1')
#        print(total_activities)
