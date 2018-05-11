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
        CREATE TABLE users (
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
    print(user_data)
    return user_data


def insert_user_data(con, cursor, user_data):
    insert_sql = """
        INSERT INTO users (name, email, password)
        VALUES (?, ?, ?)
    """
    print(user_data)
    print(user_data['name'])
    cursor.execute(insert_sql, (user_data['name'],
                                user_data['email'],
                                user_data['password']))
    con.commit()
    con.close()


def get_user_data():
    username = input('Enter username of the user: ')
    return username


def select_user_data(cursor, username):
    select_sql = """
        SELECT name, email, password FROM users
    """
    cursor.execute(select_sql)
    user_data = cursor.fetchall()
    return user_data


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
        new_username = get_user_data()
        print(select_user_data(new_cursor, new_username))
