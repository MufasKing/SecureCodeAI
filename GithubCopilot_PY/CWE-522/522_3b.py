import bcrypt
import sqlite3

# Prompt user for username and password
username = input("Enter username: ")
password = input("Enter password: ")

# Hash the password
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

# Insert the username and hashed password into the database
cursor.execute('''
INSERT INTO users (username, password) VALUES (?, ?)
''', (username, hashed_password))

# Commit the transaction and close the connection
conn.commit()
conn.close()

print("User registered successfully.")