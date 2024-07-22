import sqlite3
import bcrypt
import os

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create a table for storing user information
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password BLOB NOT NULL
)
''')
conn.commit()

def validate_input(username, password):
    if not username or not password:
        raise ValueError("Username and password cannot be empty")
    if len(username) < 3 or len(password) < 8:
        raise ValueError("Username must be at least 3 characters and password at least 8 characters long")
    # Add more validation as needed (e.g., regex for valid usernames/passwords)

def register_user(username, password):
    try:
        # Validate the input
        validate_input(username, password)

        # Generate salt
        salt = os.urandom(16)

        # Hash the password with the salt
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Store the username and hashed password in the database
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        print("User registered successfully!")

    except sqlite3.IntegrityError:
        print("Error: Username already exists.")
    except ValueError as ve:
        print(f"Input validation error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Sample usage
username = input("Enter username: ")
password = input("Enter password: ")

register_user(username, password)

# Close the database connection
conn.close()