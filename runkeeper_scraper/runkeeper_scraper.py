import argparse
import getpass
import requests

from runkeeper_user import RunkeeperUser


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get info from runkeeper site')
    parser.add_argument('email', metavar='email',
                        help='the username is your e-mail address')
    args = parser.parse_args()

    my_password = getpass.getpass()

    with requests.Session() as session:
        my_user = RunkeeperUser(args.email, my_password, session)

        print('User Profile: {}'.format(my_user.profile_name))
        print('Total Distance: {}'.format(my_user.total_distance))
        print('Total Activities: {}'.format(my_user.total_activities))
        print('Total Calories: {}'.format(my_user.total_calories))
