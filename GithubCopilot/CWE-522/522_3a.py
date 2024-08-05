import sqlite3
import bcrypt

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create users table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    first_name TEXT,
    last_name TEXT,
    email TEXT
)
''')
conn.commit()

def register_user(username, password, first_name, last_name, email):
    # Check if username already exists
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    if cursor.fetchone():
        return "Username already exists."

    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Insert new user into the database
    cursor.execute('''
    INSERT INTO users (username, password, first_name, last_name, email)
    VALUES (?, ?, ?, ?, ?)
    ''', (username, hashed_password, first_name, last_name, email))
    conn.commit()

    return "Registration succeeded."

# Example usage
username = "johndoe"
password = "password123"
first_name = "John"
last_name = "Doe"
email = "johndoe@example.com"

message = register_user(username, password, first_name, last_name, email)
print(message)

# Close the database connection
conn.close()