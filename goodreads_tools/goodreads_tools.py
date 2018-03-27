import argparse
import requests
import xmltodict
import config as cfg
import goodreads_oauth as go


def get_arguments():
    parser = argparse.ArgumentParser('Goodreads CLI tools')
    parser.add_argument('--followers', '-r', action='store_true',
                        help='Print list of followers')
    parser.add_argument('--following', '-g', action='store_true',
                        help='Print list of people user\'s following')
    parser.add_argument('--friends', '-f', action='store_true',
                        help='Print list of friends')
    parser.add_argument('--shelves', '-s', action='store_true',
                        help='Print info on user shelves')
    arguments = parser.parse_args()
    return arguments


def check_token_values():
    try:
        token_key = cfg.config['SECRETS']['TOKEN_KEY']
        token_secret = cfg.config['SECRETS']['TOKEN_SECRET']
    except KeyError:
        print('token value not found')
        print(go.save_token_values())
    return True


def check_user_id():
    try:
        user_id = cfg.config['DEFAULT']['USER_ID']
    except KeyError:
        print('user id not found')
        print(go.save_user_id())
    return True


def get_user_shelves_xml(user_id):
    url = cfg.shelves_list_url
    user_shelves_xml = requests.get(url, {'key': cfg.api_key, 'user_id': user_id}).content
    return user_shelves_xml


def get_user_shelves(user_id):
    user_shelves = []
    user_shelves_xml = get_user_shelves_xml(user_id)
    user_shelves_dict = xmltodict.parse(user_shelves_xml)['GoodreadsResponse']
    for shelf in user_shelves_dict['shelves']['user_shelf']:
        user_shelves.append(shelf)
    return user_shelves


def print_shelves_info(user_id):
    shelves = get_user_shelves(user_id)
    print('{:<20} {:<15}'.format('Shelf name', 'Books in shelf'))
    for shelf in shelves:
        print('{:<20} {:<15}'.format(shelf['name'], shelf['book_count']['#text']))


def print_friends_list(user_id):
    friends_list = go.get_friends_list(user_id)
    for friend_name in sorted(friends_list):
        print(friend_name)


def print_followers_list(user_id):
    followers_list = go.get_followers_list(user_id)
    for follower_name in sorted(followers_list):
        print(follower_name)


def print_following_list(user_id):
    following_list = go.get_following_list(user_id)
    for following_name in sorted(following_list):
        print(following_name)


if __name__ == '__main__':
    args = get_arguments()

    check_token_values()
    check_user_id()

    # just printing user_id
    my_user_id = cfg.config['DEFAULT']['USER_ID']
    print('My user id: {}'.format(my_user_id))

    if args.following:
        print_following_list(my_user_id)

    if args.followers:
        print_followers_list(my_user_id)

    if args.shelves:
        print_shelves_info(my_user_id)

    if args.friends:
        print_friends_list(my_user_id)
