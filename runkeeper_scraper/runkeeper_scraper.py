import argparse
import getpass
import requests

from runkeeper_user import RunkeeperUser


def get_activites_by_month_year(date):
    print("Activities in month/year: {}".format(date))
    month = date.split('/')[0]
    year = date.split('/')[1]
    my_activities = my_user.get_activities_by_month_year(month, year)
    for my_activity in my_activities[year][month]:
        print(my_activity)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get info from runkeeper site')
    parser.add_argument('email', metavar='email',
                        help='the username is your e-mail address')
    parser.add_argument('--get_activities_by_month', '-m', type=str, dest="date",
                        help='print all activities in "Month/Year", ex: "Jan/2016"')
    args = parser.parse_args()

    my_password = getpass.getpass()

    with requests.Session() as session:
        my_user = RunkeeperUser(args.email, my_password, session)

        print('User Profile: {}'.format(my_user.profile_name))
        print('Total Distance: {}'.format(my_user.total_distance))
        print('Total Activities: {}'.format(my_user.total_activities))
        print('Total Calories: {}'.format(my_user.total_calories))

        if args.date:
            get_activites_by_month_year(args.date)
