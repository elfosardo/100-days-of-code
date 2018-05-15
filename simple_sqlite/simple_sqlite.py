import argparse
import config
import getpass
from pathlib import Path
import sqlite3


def get_arguments():
    parser = argparse.ArgumentParser('Simple users management with SQLite')
    parser.add_argument('--print_tables', '-t', action='store_true',
                        help='Show all the tables in the database')
    parser.add_argument('--add_user_data', '-a', action='store_true',
                        help='Add new user data')
    parser.add_argument('--get_user_data', '-u', action='store_true',
                        help='Get info from a user')
    arguments = parser.parse_args()
    return arguments


def db_connect(db_path=config.DB_PATH):
    con = sqlite3.connect(db_path)
    return con


def init_db():
    print('Initializing Database structure...')
    con = db_connect()
    cursor = con.cursor()
    setup_db(con, cursor)
    return True


def setup_db(con, cursor):
    cursor.execute(config.create_users__table_sql)
    con.commit()
    con.close()
    return True


def print_tables(cursor):

    cursor.execute(config.select_table_sql)
    print(cursor.fetchall())
    return True


def add_user_data():
    username = input('Enter name of the new user: ')
    email = input('Enter email of the new user: ')
    password = getpass.getpass('Password of the new user: ')
    user_data = {'name': username,
                 'email': email,
                 'password': password}
    return user_data


def insert_user_data(con, cursor, user_data):
    cursor.execute(config.insert_into_users_sql, (user_data['name'],
                                                  user_data['email'],
                                                  user_data['password']))
    con.commit()
    con.close()
    return True


def ask_user_name():
    username = input('Enter username of the user: ')
    return username


def get_user_data(cursor, username):
    cursor.execute(config.select_from_users_sql, (username,))
    user_data = cursor.fetchall()
    return user_data


def print_user_data(user_data):
    formatted_data = [f'{username:<12}{email:<20}{password:>15}'
                      for username, email, password in user_data]
    username, email, password = 'Username', 'Email', 'Password'
    print('\n'.join([f'{username:<12}{email:<20}{password:>15}'] +
                    formatted_data))
    return True


if __name__ == '__main__':
    args = get_arguments()

    mydb_path = Path(config.DB_PATH)
    if not mydb_path.exists():
        init_db()

    new_con = db_connect()
    new_cursor = new_con.cursor()

    if args.print_tables:
        print_tables(new_cursor)

    if args.add_user_data:
        new_user_data = add_user_data()
        insert_user_data(new_con, new_cursor, new_user_data)

    if args.get_user_data:
        new_username = ask_user_name()
        my_user_data = get_user_data(new_cursor, new_username)
        print_user_data(my_user_data)
