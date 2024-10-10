import hashlib
import os
import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('user_database.db')
cursor = conn.cursor()

# Create a table to store usernames and their hashed passwords
cursor.execute('''CREATE TABLE IF NOT EXISTS users
               (username TEXT UNIQUE, password_hash TEXT)''')
conn.commit()

def hash_password(password, salt=None):
    """Hash a password with an optional salt."""
    if salt is None:
        salt = os.urandom(16)  # Generate a new salt
    hasher = hashlib.sha256()
    hasher.update(salt + password.encode('utf-8'))  # Concatenate salt and password before hashing
    return salt + hasher.digest()

def register_user(username, password):
    """Register a new user with a username and password."""
    if not username or not password:
        raise ValueError("Username and password cannot be empty.")
    
    # Hash the password with a new salt
    password_hash = hash_password(password)
    
    try:
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
        conn.commit()
    except sqlite3.IntegrityError:
        raise ValueError("Username already exists.")
    
    print("User registered successfully.")

# Example usage
try:
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    
    # Simple input validation
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long.")
    
    register_user(username, password)
except ValueError as e:
    print(e)