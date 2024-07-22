import sqlite3
import bcrypt

def create_table_if_not_exists(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            hashed_password BLOB NOT NULL
        )
    ''')
    conn.commit()

def hash_password(password):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def insert_user(conn, username, hashed_password):
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO users (username, hashed_password) VALUES (?, ?)
        ''', (username, hashed_password))
        conn.commit()
        print("User added successfully.")
    except sqlite3.IntegrityError:
        print("Error: Username already exists.")

def main():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('user_data.db')
    
    # Create the table if it does not exist
    create_table_if_not_exists(conn)
    
    # Get user input
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    # Hash the password
    hashed_password = hash_password(password)
    
    # Insert the user into the database
    insert_user(conn, username, hashed_password)
    
    # Close the connection
    conn.close()

if __name__ == '__main__':
    main()
