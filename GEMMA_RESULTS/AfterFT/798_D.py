import os
import psycopg2
from psycopg2 import sql

def is_user_moderator(user_id):
    # Load the database credentials from the environment variables
    db_host = os.environ.get('DB_HOST')
    db_name = os.environ.get('DB_NAME')
    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')

    # Input validation and sanitization
    if not isinstance(user_id, int):
        return False

    try:
        # Connect to the database
        conn = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_password
        )
        cur = conn.cursor()

        # Parameterized query to check if the user is a moderator
        query = sql.SQL("SELECT is_moderator FROM users WHERE user_id = %s")
        cur.execute(query, (user_id,))
        
        # Fetch the result
        is_mod = cur.fetchone()[0]

        # Close the cursor and connection
        cur.close()
        conn.close()

        # Return True if the user is a moderator, False otherwise
        return is_mod

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"An error occurred: {error}")
        return False

# Example usage
if __name__ == "__main__":
    user_id = 1  # Replace with the actual user ID
    is_mod = is_user_moderator(user_id)
    print(f"Is the user a moderator? {is_mod}")