import sqlite3

def check_username_exists(username):
    # Establish a connection to the database
    conn = sqlite3.connect('example.db')  # Replace 'example.db' with your database file
    cursor = conn.cursor()
    
    # Execute a query to check if the username exists
    cursor.execute("SELECT 1 FROM users WHERE username = ?", (username,))
    
    # Fetch the result
    result = cursor.fetchone()
    
    # Close the cursor and connection
    cursor.close()
    conn.close()
    
    # Return True if username exists, otherwise False
    return result is not None

# Example usage
username = 'test_user'
exists = check_username_exists(username)
print(f"Does the username exist? {exists}")