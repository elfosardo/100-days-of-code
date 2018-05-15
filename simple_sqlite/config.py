import os

DB_PATH = os.path.join(os.path.dirname(__file__), './users.sqlite')

create_users__table_sql = """
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT unique,
    password TEXT)
"""

insert_into_users_sql = """
    INSERT INTO users (name, email, password)
    VALUES (?, ?, ?)
"""

select_from_users_sql = """
    SELECT name, email, password FROM users WHERE name=?
"""

select_table_sql = "SELECT name FROM sqlite_master WHERE type='table'"
