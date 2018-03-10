import argparse
import requests
import xmltodict
import config as cfg


def get_arguments():
    parser = argparse.ArgumentParser('Goodreads python wrapper')
    parser.add_argument('book_name',
                        help='Name of the book to search')
    arguments = parser.parse_args()
    return arguments


def get_user_shelves_xml():
    url = '{}/shelf/list.xml'.format(cfg.API_URL)
    user_shelves_xml = requests.get(url, {'key': cfg.api_key, 'user_id': cfg.user_id}).content
    return user_shelves_xml


def get_user_shelves():
    user_shelves = []
    user_shelves_xml = get_user_shelves_xml()
    user_shelves_dict = xmltodict.parse(user_shelves_xml)['GoodreadsResponse']
    for shelf in user_shelves_dict['shelves']['user_shelf']:
        user_shelves.append(shelf)
    return user_shelves


if __name__ == '__main__':
    args = get_arguments()

    my_shelves = get_user_shelves()

    print('{:<20} {:<15}'.format('Shelf name', 'Books in shelf'))

    for shelf in my_shelves:
        print('{:<20} {:<15}'.format(shelf['name'], shelf['book_count']['#text']))
