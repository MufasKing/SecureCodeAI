import sqlite3
import hashlib

def main():
    # Get username and password from user
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Hash password using SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Insert username and hashed password into database
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()