import sqlite3
import hashlib
import os

# Function to create the database and users table
def create_database():
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Function to hash password with salt
def hash_password(password, salt):
    hasher = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return hasher

# Function to register a new user
def register_user(username, password):
    salt = os.urandom(16)  # Generate a new salt
    hashed_password = hash_password(password, salt)
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    try:
        c.execute('''
            INSERT INTO users (username, password)
            VALUES (?, ?)
        ''', (username, salt + hashed_password))  # Store the salt and hashed password
        conn.commit()
        print('User registered successfully!')
    except sqlite3.IntegrityError:
        print('Username already exists.')
    finally:
        conn.close()

# Function to verify user login
def verify_user(username, password):
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute('''
        SELECT password FROM users WHERE username = ?
    ''', (username,))
    result = c.fetchone()
    conn.close()
    if result is None:
        print('Username does not exist.')
        return False
    
    stored_password = result[0]
    salt = stored_password[:16]  # Extract the salt from stored password
    hashed_password = stored_password[16:]  # Extract the hashed password
    
    new_hashed_password = hash_password(password, salt)
    if new_hashed_password == hashed_password:
        print('Login successful!')
        return True
    else:
        print('Incorrect password.')
        return False

# Main function to interact with the user
def main():
    create_database()
    while True:
        action = input('Do you want to (register) or (login)? ').strip().lower()
        if action not in ['register', 'login']:
            print('Invalid action. Please choose "register" or "login".')
            continue
        
        username = input('Username: ').strip()
        password = input('Password: ').strip()

        if action == 'register':
            register_user(username, password)
        elif action == 'login':
            verify_user(username, password)

if __name__ == '__main__':
    main()
