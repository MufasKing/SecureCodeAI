import os
import hashlib
import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create a table for storing user data
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')
conn.commit()

def hash_password(password):
    # Generate a random salt
    salt = os.urandom(16)
    # Hash the password with the salt
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    # Concatenate the salt and hashed password
    salted_hashed_password = salt + hashed_password
    return salted_hashed_password

def register_user(username, password):
    # Hash the password
    salted_hashed_password = hash_password(password)
    # Store the username and salted hashed password in the database
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, salted_hashed_password))
    conn.commit()

# Example usage
username = input("Enter username: ")
password = input("Enter password: ")
register_user(username, password)

# Close the database connection
conn.close()