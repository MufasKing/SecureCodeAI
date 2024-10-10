import hashlib
import os
import sqlite3

# Function to generate a random salt
def generate_salt():
    return os.urandom(16)

# Function to hash the password with the salt
def hash_password(password, salt):
    return hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)

# Function to store the username, hashed password, and salt in the database
def register_user(username, password):
    salt = generate_salt()
    hashed_password = hash_password(password, salt)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (username TEXT, password BLOB, salt BLOB)''')
    cursor.execute('INSERT INTO users (username, password, salt) VALUES (?, ?, ?)',
                   (username, hashed_password, salt))
    conn.commit()
    conn.close()

# Function to verify the password during login
def verify_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT password, salt FROM users WHERE username = ?', (username,))
    result = cursor.fetchone()
    conn.close()
    if result:
        stored_password, salt = result
        return stored_password == hash_password(password, salt)
    return False

# Example usage
if __name__ == "__main__":
    # Register a new user
    register_user('user1', 'password123')

    # Verify the user
    if verify_user('user1', 'password123'):
        print("Login successful")
    else:
        print("Login failed")