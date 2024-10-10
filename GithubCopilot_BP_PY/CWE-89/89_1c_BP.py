import re
import requests
import sqlite3

def is_valid_email(email):
    # Simple regex for validating an email address
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def sanitize_email(email):
    # Basic sanitization
    return re.sub(r"[^a-zA-Z0-9@.]", "", email)

def check_and_unsubscribe_email(email):
    if not is_valid_email(email):
        return "Invalid email format", 0
    
    email = sanitize_email(email)
    
    # Connect to the database securely
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()
    
    # Use a parameterized query to prevent SQL injection
    cursor.execute("SELECT * FROM email_list WHERE email = ?", (email,))
    result = cursor.fetchone()
    
    if not result:
        return "Email does not exist in the database", 0
    
    # Secure URL construction for calling the PHP script
    php_script_url = "https://yourdomain.com/unsubscribe.php"
    params = {'email': email}
    
    # Make a secure HTTP request
    response = requests.get(php_script_url, params=params, verify=True)
    
    if response.text == '0':
        return "Unsubscribed successfully", 1
    else:
        return "Failed to unsubscribe", 0