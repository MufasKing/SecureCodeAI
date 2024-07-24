import sqlite3
from bcrypt import hashpw, gensalt, checkpw
import re

def validate_password(password):
    # Basic password validation
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter"
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter"
    if not re.search(r'[0-9]', password):
        return False, "Password must contain at least one number"
    if not re.search(r'[\W_]', password):
        return False, "Password must contain at least one special character"
    return True, ""

def hash_password(password):
    return hashpw(password.encode('utf-8'), gensalt())

def insert_user(username, password_hash):
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL
            )
        ''')
        cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', (username, password_hash))
        conn.commit()
    except sqlite3.IntegrityError as e:
        return False, f"Database error: {e}"
    except Exception as e:
        return False, f"An unexpected error occurred: {e}"
    finally:
        conn.close()
    return True, "User registered successfully"

def register_user(username, password):
    is_valid, message = validate_password(password)
    if not is_valid:
        return False, message
    password_hash = hash_password(password)
    return insert_user(username, password_hash)

def main():
    username = input("Enter username: ")
    password = input("Enter password: ")
    success, message = register_user(username, password)
    print(message)

if __name__ == '__main__':
    main()