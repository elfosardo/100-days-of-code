import argparse
import requests
import xmltodict
import config as cfg
import goodreads_oauth as go


def get_arguments():
    parser = argparse.ArgumentParser('Goodreads CLI tools')
    parser.add_argument('--books', '-b', action='store_true',
                        help='Print list of owned books')
    parser.add_argument('--followers', '-r', action='store_true',
                        help='Print list of followers')
    parser.add_argument('--following', '-g', action='store_true',
                        help='Print list of people user\'s following')
    parser.add_argument('--friends', '-f', action='store_true',
                        help='Print list of friends')
    parser.add_argument('--shelves', '-s', action='store_true',
                        help='Print info on user shelves')
    parser.add_argument('--show_owned_book', '-o', action='store_true',
                        help='Show info on an owned book by owned book id')
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
    user_shelves_xml = requests.get(url, {'key': cfg.api_key,
                                          'user_id': user_id}).content
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
        print('{:<20} {:<15}'.format(shelf['name'],
                                     shelf['book_count']['#text']))


def execute_command(user_id):
    list_to_order = []
    if args.shelves:
        print_shelves_info(user_id)
    elif args.following:
        list_to_order = go.get_following_list(user_id)
    elif args.followers:
        list_to_order = go.get_followers_list(user_id)
    elif args.friends:
        list_to_order = go.get_friends_list(user_id)
    elif args.books:
        books_list = go.get_books_owned(user_id)
        print_book_info(books_list)
    elif args.show_owned_book:
        owned_book_id = input('Owned Book ID: ')
        go.show_owned_book(owned_book_id)
    if len(list_to_order) > 0:
        print_ordered_list(list_to_order)


def print_ordered_list(list_to_order):
    for element in sorted(list_to_order):
        print(element)


def print_book_info(books_list):
    print('{:<13} {:>9} {} | {}'.format('Owned Book ID',
                                        'Book ID',
                                        'Book Title',
                                        'Book Authors'))
    for book in books_list:
        print('{:<13} {:>9} {} | {}'.format(book.owned_id,
                                            book.id,
                                            book.title,
                                            *book.authors, sep=', '))


if __name__ == '__main__':
    args = get_arguments()

    check_token_values()
    check_user_id()

    # just printing user_id
    my_user_id = cfg.config['DEFAULT']['USER_ID']
    print('My user id: {}'.format(my_user_id))

    execute_command(my_user_id)
