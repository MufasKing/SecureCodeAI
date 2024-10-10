import os
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Environment variables
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

def check_username_exists(username):
    connection = None
    cursor = None
    try:
        # Establish a secure database connection
        connection = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = connection.cursor()

        # Parameterized query to check if username exists
        query = sql.SQL("SELECT 1 FROM users WHERE username = %s")
        cursor.execute(query, (username,))

        # Check if any rows are returned
        result = cursor.fetchone()
        if result:
            return True
        else:
            return False
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
        return False
    finally:
        # Close the cursor and connection to clean up
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Example usage
if __name__ == "__main__":
    username_to_check = "example_user"
    user_exists = check_username_exists(username_to_check)
    print(f"Does the user exist? {user_exists}")