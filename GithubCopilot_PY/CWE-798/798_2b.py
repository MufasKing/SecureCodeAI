import os
import psycopg2
from psycopg2 import sql

def is_user_moderator(user_id):
    try:
        # Fetch database credentials from environment variables
        db_name = os.getenv('DB_NAME')
        db_user = os.getenv('DB_USER')
        db_password = os.getenv('DB_PASSWORD')
        db_host = os.getenv('DB_HOST')
        db_port = os.getenv('DB_PORT')

        # Establish database connection
        connection = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )

        # Create a cursor object
        cursor = connection.cursor()

        # Execute the query to check if the user is a moderator
        query = sql.SQL("SELECT is_moderator FROM users WHERE user_id = %s")
        cursor.execute(query, (user_id,))

        # Fetch the result
        result = cursor.fetchone()

        # Return True if the user is a moderator, False otherwise
        if result and result[0]:
            return True
        else:
            return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

    finally:
        # Close the connection
        if connection:
            cursor.close()
            connection.close()