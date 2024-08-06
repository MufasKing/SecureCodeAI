import bcrypt
import psycopg2
from psycopg2 import sql

def hash_password(password):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def insert_user(username, password, connection):
    hashed_password = hash_password(password)
    try:
        with connection.cursor() as cursor:
            query = sql.SQL("INSERT INTO users (username, password) VALUES (%s, %s)")
            cursor.execute(query, (username, hashed_password))
            connection.commit()
    except psycopg2.Error as e:
        print(f"An error occurred: {e}")
        connection.rollback()

def validate_password(password):
    # Implement your password validation logic here
    # For example, check length, special characters, etc.
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long")
    # Add more validation rules as needed
    return True

def main():
    # Connect to your database
    connection = psycopg2.connect(
        dbname="your_dbname",
        user="your_username",
        password="your_password",
        host="your_host"
    )

    try:
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        if validate_password(password):
            insert_user(username, password, connection)
            print("User successfully added.")
    except ValueError as ve:
        print(f"Validation error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        connection.close()

if __name__ == "__main__":
    main()