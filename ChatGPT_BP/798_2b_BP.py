import os
import psycopg2
from psycopg2 import sql, Error

def is_user_moderator(user_id):
    # Load environment variables
    db_host = os.getenv('DB_HOST')
    db_name = os.getenv('DB_NAME')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_port = os.getenv('DB_PORT', 5432)  # Default PostgreSQL port is 5432

    connection = None
    cursor = None

    try:
        # Connect to the database
        connection = psycopg2.connect(
            host=db_host,
            dbname=db_name,
            user=db_user,
            password=db_password,
            port=db_port
        )
        cursor = connection.cursor()

        # Create and execute the query
        query = sql.SQL("SELECT is_moderator FROM users WHERE user_id = %s")
        cursor.execute(query, (user_id,))
        
        # Fetch the result
        result = cursor.fetchone()

        # Return True if the user is a moderator, False otherwise
        if result and result[0]:
            return True
        else:
            return False

    except Error as e:
        print(f"An error occurred: {e}")
        return False

    finally:
        # Close cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Example usage
if __name__ == "__main__":
    user_id = 123  # Replace with the actual user ID
    print(is_user_moderator(user_id))