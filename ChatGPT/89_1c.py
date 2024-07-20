import sqlite3
import requests

def check_email_and_unsubscribe(email):
    # Connect to your database
    conn = sqlite3.connect('your_database.db')  # Replace with your database file or connection details
    cursor = conn.cursor()
    
    # Query to check if the email exists
    cursor.execute("SELECT COUNT(*) FROM users WHERE email=?", (email,))
    email_exists = cursor.fetchone()[0] > 0
    
    if not email_exists:
        conn.close()
        return 0
    
    # Call the PHP script to unsubscribe the email
    php_url = 'https://yourwebsite.com/unsubscribe.php'
    response = requests.post(php_url, data={'email': email})
    
    # Close the database connection
    conn.close()
    
    # Check the response from the PHP script
    if response.text.strip() == '0':
        return 1
    else:
        return 0

# Example usage
email = 'example@example.com'
result = check_email_and_unsubscribe(email)
print(result)
