import os
import mysql.connector
from mysql.connector import errorcode

# Function to validate environment variables
def validate_env_vars():
    required_env_vars = ['MYSQL_HOST', 'MYSQL_USER', 'MYSQL_PASSWORD', 'MYSQL_DB']
    for env_var in required_env_vars:
        if not env_var in os.environ:
            raise Exception(f"Environment variable '{env_var}' is not set.")

# Function to connect to the MySQL database
def connect_to_db() -> mysql.connector.cursor:
    try:
        db_connection = mysql.connector.connect(
            host=os.environ['MYSQL_HOST'],
            user=os.environ['MYSQL_USER'],
            password=os.environ['MYSQL_PASSWORD'],
            database=os.environ['MYSQL_DB']
        )
        if db_connection.is_connected():
            db_info = "Connected to MySQL database: " + db_connection.get_database()
            print(db_info)
            return db_connection.cursor()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    return None

# Function to check if a user is a moderator
def is_moderator(user_id: int) -> bool:
    # Validate input
    if not isinstance(user_id, int):
        return False

    # Validate environment variables
    validate_env_vars()

    # Connect to the database
    with connect_to_db() as cursor:
        if cursor:
            # Use parameterization to prevent SQL injection
            query = "SELECT is_moderator FROM users WHERE user_id = %s"
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()

            if result:
                return result[0]
            else:
                return False

# Example usage
user_id = 123  # Replace with the actual user ID
if is_moderator(user_id):
    print("User is a moderator")
else:
    print("User is not a moderator")