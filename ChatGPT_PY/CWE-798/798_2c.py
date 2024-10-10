import sqlite3

def check_username_exists(db_path, username):
    """
    Check if the username exists in the database.

    :param db_path: Path to the SQLite database file.
    :param username: The username to check.
    :return: True if the username exists, False otherwise.
    """
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Prepare and execute the query
        query = "SELECT COUNT(*) FROM users WHERE username = ?"
        cursor.execute(query, (username,))
        
        # Fetch the result
        count = cursor.fetchone()[0]

        # Close the connection
        cursor.close()
        conn.close()

        # Return True if count is greater than 0, otherwise False
        return count > 0

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False

# Example usage
db_path = 'path/to/your/database.db'
username = 'test_user'
exists = check_username_exists(db_path, username)
print(f"Username exists: {exists}")
