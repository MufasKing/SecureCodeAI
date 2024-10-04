import sqlite3
import hashlib
import re

# Define a regular expression pattern to validate usernames
USERNAME_PATTERN = r'^[a-zA-Z0-9_]{3,20}$'

# Define a regular expression pattern to validate passwords
PASSWORD_PATTERN = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=])[\w@#$%^&+=]{8,}$'

# Connect to the SQLite database
with sqlite3.connect("users.db") as db:
    cursor = db.cursor()

    # Create a table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT NOT NULL UNIQUE, 
            password_hash TEXT NOT NULL
        );
    ''')
    db.commit()

def register_user(username, password):
    # Validate the username
    if not re.match(USERNAME_PATTERN, username):
        raise ValueError("Invalid username. Username must be between 3 and 20 alphanumeric characters or underscores.")

    # Validate the password
    if not re.match(PASSWORD_PATTERN, password):
        raise ValueError("Invalid password. Password must be at least 8 characters long and contain at least one number, one uppercase letter, one lowercase letter, and one special character.")

    # Hash the password
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    try:
        # Insert the username and hashed password into the database
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
        db.commit()
        print("User registered successfully.")
    except sqlite3.IntegrityError:
        print("Error: Username already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
try:
    register_user("valid_username", "SecurePassword123@")
except ValueError as e:
    print(e)