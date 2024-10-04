import sqlite3
import bcrypt
import re

# Connect to the database
with sqlite3.connect("users.db") as db:
    cursor = db.cursor()

# Input validation
def validate_username(username):
    if not re.match(r'^[a-zA-Z0-9_]{3,20}$', username):
        raise ValueError("Username must be between 3 and 20 characters long and contain only alphanumeric characters or underscores.")

def validate_password(password):
    if not re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=])[\w@#$%^&+=]{8,}$', password):
        raise ValueError("Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")

# Password hashing
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# Input sanitization
def sanitize_input(input_string):
    sanitized_string = re.sub(r'[^a-zA-Z0-9@#$%^&+=_. ]', '', input_string)
    return sanitized_string.strip()

# Insert into database
def insert_user(username, password_hash):
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password_hash))
        db.commit()
    except sqlite3.IntegrityError:
        print("Error: Username already exists.")
    except Exception as e:
        print(f"Error: {str(e)}")

# User interface
try:
    username = sanitize_input(input("Enter username: "))
    validate_username(username)
    password = sanitize_input(input("Enter password: "))
    validate_password(password)
    password_hash = hash_password(password)
    insert_user(username, password_hash)
except ValueError as e:
    print(f"Error: {str(e)}")