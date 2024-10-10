import os
import psycopg2
from psycopg2 import sql
from psycopg2.extras import RealDictCursor

def is_user_moderator(user_id):
    # Load database credentials from environment variables
    db_host = os.getenv('DB_HOST')
    db_name = os.getenv('DB_NAME')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')

    # SQL query to check if the user is a moderator
    query = sql.SQL("SELECT is_moderator FROM users WHERE user_id = %s")

    try:
        # Connect to the database
        with psycopg2.connect(
            host=db_host,
            dbname=db_name,
            user=db_user,
            password=db_password
        ) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                # Execute the query
                cur.execute(query, (user_id,))
                result = cur.fetchone()

                # Check if the user is a moderator
                if result and result['is_moderator']:
                    return True
                else:
                    return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        # Ensure the database connection is closed
        if conn:
            conn.close()

# Example usage
user_id = 1
print(is_user_moderator(user_id))