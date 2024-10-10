import bcrypt
import sqlite3

def hash_password(password):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def insert_user(username, hashed_password):
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    
    # Insert the new user
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        print(f"User '{username}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"Error: Username '{username}' already exists.")
    
    # Close the connection
    conn.close()

def main():
    # Get username and password from the user
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    # Hash the password
    hashed_password = hash_password(password)
    
    # Insert username and hashed password into the database
    insert_user(username, hashed_password.decode('utf-8'))

if __name__ == '__main__':
    main()
