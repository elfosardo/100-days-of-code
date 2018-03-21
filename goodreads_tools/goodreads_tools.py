import requests
import xmltodict
import config as cfg
import goodreads_oauth as go


def get_user_shelves_xml(user_id):
    url = '{}/shelf/list.xml'.format(cfg.API_URL)
    user_shelves_xml = requests.get(url, {'key': cfg.api_key, 'user_id': user_id}).content
    return user_shelves_xml


def get_user_shelves(user_id):
    user_shelves = []
    user_shelves_xml = get_user_shelves_xml(user_id)
    user_shelves_dict = xmltodict.parse(user_shelves_xml)['GoodreadsResponse']
    for shelf in user_shelves_dict['shelves']['user_shelf']:
        user_shelves.append(shelf)
    return user_shelves


if __name__ == '__main__':
    try:
        token_key = cfg.config['SECRETS']['TOKEN_KEY']
        token_secret = cfg.config['SECRETS']['TOKEN_SECRET']
    except KeyError:
        print('token value not found')
        print(go.get_token_values())

    try:
        my_user_id = cfg.config['DEFAULT']['USER_ID']
    except KeyError:
        print('user id not found')
        print(go.save_user_id())

    # testing user_id in config file
    my_user_id = cfg.config['DEFAULT']['USER_ID']
    print('My user id: {}'.format(my_user_id))

    my_shelves = get_user_shelves(my_user_id)

    print('{:<20} {:<15}'.format('Shelf name', 'Books in shelf'))

    for my_shelf in my_shelves:
        print('{:<20} {:<15}'.format(my_shelf['name'], my_shelf['book_count']['#text']))
