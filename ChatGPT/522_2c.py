import os
import hashlib
import sqlite3

def generate_salt(length=16):
    """Generate a secure random salt."""
    return os.urandom(length)

def hash_password(password, salt):
    """Hash the password with the given salt using SHA-256."""
    hasher = hashlib.sha256()
    hasher.update(salt + password.encode('utf-8'))
    return hasher.digest()

def store_user(username, password):
    """Store the username and hashed password in the database."""
    # Generate a salt and hash the password
    salt = generate_salt()
    hashed_password = hash_password(password, salt)
    
    # Concatenate salt and hashed password
    salted_hashed_password = salt + hashed_password

    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            salted_hashed_password BLOB
        )
    ''')
    
    # Insert the user into the database
    cursor.execute('''
        INSERT INTO users (username, salted_hashed_password)
        VALUES (?, ?)
    ''', (username, salted_hashed_password))
    
    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

def main():
    """Main function to register a user."""
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    store_user(username, password)
    print("User registered successfully!")

if __name__ == "__main__":
    main()
