import sqlite3
import bcrypt

def create_table():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Create table for storing users if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            hashed_password TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

def hash_password(password: str) -> str:
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def insert_user(username: str, hashed_password: str):
    # Connect to SQLite database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Insert username and hashed password into the database
    cursor.execute('''
        INSERT INTO users (username, hashed_password)
        VALUES (?, ?)
    ''', (username, hashed_password))

    conn.commit()
    conn.close()

def main():
    create_table()
    
    # Get username and password from user
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Hash the password
    hashed_password = hash_password(password)

    # Insert the user into the database
    insert_user(username, hashed_password)

    print("User successfully added!")

if __name__ == "__main__":
    main()
