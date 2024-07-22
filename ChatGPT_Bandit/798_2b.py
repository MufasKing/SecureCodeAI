import os
import psycopg2
from psycopg2 import sql

def is_user_moderator(user_id):
    try:
        # Retrieve database credentials from environment variables
        db_name = os.getenv('DB_NAME')
        db_user = os.getenv('DB_USER')
        db_password = os.getenv('DB_PASSWORD')
        db_host = os.getenv('DB_HOST')
        db_port = os.getenv('DB_PORT', '5432')  # Default PostgreSQL port is 5432

        # Establish a connection to the database
        connection = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        
        # Create a cursor object
        cursor = connection.cursor()
        
        # Define the SQL query
        query = sql.SQL("SELECT is_moderator FROM users WHERE user_id = %s;")
        
        # Execute the SQL query
        cursor.execute(query, (user_id,))
        
        # Fetch the result
        result = cursor.fetchone()
        
        # Check if the result is not None and is_moderator is True
        if result is not None and result[0]:
            return True
        else:
            return False
        
    except Exception as error:
        print(f"An error occurred: {error}")
        return False
    
    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Example usage
user_id = 123  # Replace with the actual user ID
print(is_user_moderator(user_id))
