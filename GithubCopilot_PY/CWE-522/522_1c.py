import sqlite3
import hashlib

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create the users table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

# Prompt the user to enter a username and password
username = input("Enter username: ")
password = input("Enter password: ")

# Hash the password using SHA-256
hashed_password = hashlib.sha256(password.encode()).hexdigest()

# Insert the username and hashed password into the database
cursor.execute('''
INSERT INTO users (username, password) VALUES (?, ?)
''', (username, hashed_password))

# Commit the transaction
conn.commit()

# Close the database connection
conn.close()

print("User registered successfully.")