import argparse
import getpass
import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__), './users.sqlite')


def get_arguments():
    parser = argparse.ArgumentParser('Simple users management with SQLite')
    parser.add_argument('--setup', '-s', action='store_true',
                        help='Initialize database')
    parser.add_argument('--print_tables', '-t', action='store_true',
                        help='Show all the tables in the database')
    parser.add_argument('--add_user_data', '-a', action='store_true',
                        help='Add new user data')
    parser.add_argument('--get_user_data', '-u', action='store_true',
                        help='Get info from a user')
    arguments = parser.parse_args()
    return arguments


def db_connect(db_path=DB_PATH):
    con = sqlite3.connect(db_path)
    return con


def setup_db(con, cursor):
    users_sql = """
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT unique,
        password TEXT)
    """
    cursor.execute(users_sql)
    con.commit()
    con.close()
    return True


def print_tables(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    print(cursor.fetchall())


def add_user_data():
    user_data = {}
    user_data['name'] = input('Enter name of the new user: ')
    user_data['email'] = input('Enter email of the new user: ')
    user_data['password'] = getpass.getpass('Password of the new user: ')
    return user_data


def insert_user_data(con, cursor, user_data):
    insert_sql = """
        INSERT INTO users (name, email, password)
        VALUES (?, ?, ?)
    """
    cursor.execute(insert_sql, (user_data['name'],
                                user_data['email'],
                                user_data['password']))
    con.commit()
    con.close()


def ask_user_name():
    username = input('Enter username of the user: ')
    return username


def get_user_data(cursor, username):
    select_sql = """
        SELECT name, email, password FROM users WHERE name=?
    """
    cursor.execute(select_sql, (username,))
    user_data = cursor.fetchall()
    return user_data


def print_user_data(user_data):
    formatted_data = [f'{username:<12}{email:<20}{password:>15}'
                      for username, email, password in user_data]
    username, email, password = 'Username', 'Email', 'Password'
    print('\n'.join([f'{username:<12}{email:<20}{password:>15}'] +
                    formatted_data))


if __name__ == '__main__':
    args = get_arguments()

    new_con = db_connect()
    new_cursor = new_con.cursor()

    if args.setup:
        setup_db(new_con, new_cursor)

    if args.print_tables:
        print_tables(new_cursor)

    if args.add_user_data:
        new_user_data = add_user_data()
        insert_user_data(new_con, new_cursor, new_user_data)

    if args.get_user_data:
        new_username = ask_user_name()
        my_user_data = get_user_data(new_cursor, new_username)
        print_user_data(my_user_data)
