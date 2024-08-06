import sqlite3
import hashlib
import os
from sqlite3 import Error

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def create_user(conn, user):
    """Create a new user into the users table"""
    sql = ''' INSERT INTO users(username,password_hash)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()
    return cur.lastrowid

def hash_password(password):
    """Hash a password for storing."""
    salt = os.urandom(32) # A new salt for this user
    key = hashlib.pbkdf2_hmac(
        'sha256', # The hash digest algorithm for HMAC
        password.encode('utf-8'), # Convert the password to bytes
        salt, # Provide the salt
        100000 # It is recommended to use at least 100,000 iterations of SHA-256 
    )
    storage = salt + key # store the salt and key together
    return storage.hex() # return as hex string for storage

def main():
    database = r"path_to_your_database.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # Validate input
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        
        # Check if username is unique
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=?", (username,))
        if cur.fetchone():
            print("Username already exists. Please choose a different username.")
            return
        
        # Hash password
        password_hash = hash_password(password)
        
        # Insert new user
        new_user = (username, password_hash)
        try:
            create_user(conn, new_user)
            print("User created successfully.")
        except sqlite3.IntegrityError as e:
            print("Failed to create user. Error: ", e)
        except Error as e:
            print("An error occurred:", e)

if __name__ == '__main__':
    main()