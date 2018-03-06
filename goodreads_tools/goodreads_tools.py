import argparse
import requests
import config as cfg


def get_arguments():
    parser = argparse.ArgumentParser('Goodreads python wrapper')
    parser.add_argument('book_name',
                        help='Name of the book to search')
    arguments = parser.parse_args()
    return arguments


def get_user_shelves():
    url = '{}/shelf/list.xml?key={}'.format(cfg.API_URL, cfg.api_key)
    response = requests.get(url)
    return response


if __name__ == '__main__':
    args = get_arguments()

    user_shelves = get_user_shelves()

    print(user_shelves.text)
