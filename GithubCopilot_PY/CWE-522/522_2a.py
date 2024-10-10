import bcrypt
import sqlite3

# Function to hash the password
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

# Function to insert username and hashed password into the database
def insert_user(username, hashed_password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
    conn.commit()
    conn.close()

# Main function to get user input and insert into the database
def main():
    username = input("Enter username: ")
    password = input("Enter password: ")
    hashed_password = hash_password(password)
    insert_user(username, hashed_password)
    print("User registered successfully.")

if __name__ == "__main__":
    main()