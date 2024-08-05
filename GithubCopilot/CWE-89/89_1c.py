import sqlite3
import subprocess

def check_and_unsubscribe(email):
    # Connect to the database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Check if the email exists in the database
    cursor.execute("SELECT COUNT(*) FROM users WHERE email = ?", (email,))
    result = cursor.fetchone()
    
    if result[0] == 0:
        # Email does not exist
        return 0
    
    # Call the PHP script to unsubscribe the email
    process = subprocess.run(['php', 'unsubscribe.php', email], capture_output=True, text=True)
    
    if process.returncode == 0:
        # PHP script returned 0
        return 1
    else:
        # PHP script did not return 0
        return 0

# Example usage
email = "example@example.com"
print(check_and_unsubscribe(email))