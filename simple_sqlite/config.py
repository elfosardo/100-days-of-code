

DB_PATH = './users.sqlite'

create_users__table_sql = """
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT unique,
    password TEXT)
"""

delete_user_from_users_sql = """
    DELETE FROM users WHERE name=?
"""

insert_into_users_sql = """
    INSERT INTO users (name, email, password)
    VALUES (?, ?, ?)
"""

select_user_from_users_sql = """
    SELECT name, email, password FROM users WHERE name=?
"""

select_all_from_users_sql = """
    SELECT name, email, password FROM users ORDER BY name
"""

select_table_sql = "SELECT name FROM sqlite_master WHERE type='table'"
