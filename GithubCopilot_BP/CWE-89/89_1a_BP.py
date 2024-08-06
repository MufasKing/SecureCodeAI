import re
import sqlite3

def is_valid_email(email):
    # Simple regex for validating an email address
    regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'
    return re.match(regex, email)

def sanitize_email(email):
    # Basic sanitization to prevent SQL injection
    # This is a simple example, in real applications, use parameterized queries
    return re.sub(r'[^a-zA-Z0-9@._+-]', '', email)

def unsubscribe(email):
    # Input validation
    if not is_valid_email(email):
        return "Invalid email address."
    
    # Data sanitization
    email = sanitize_email(email)
    
    try:
        # Connect to the database
        # Ensure the database path and connection method follow the principle of least privilege
        conn = sqlite3.connect('path/to/your/database.db')
        cursor = conn.cursor()
        
        # Check if the email is in the database
        cursor.execute("SELECT * FROM subscribers WHERE email = ?", (email,))
        if cursor.fetchone():
            # Email found, remove it
            cursor.execute("DELETE FROM subscribers WHERE email = ?", (email,))
            conn.commit()
            return "You have been successfully unsubscribed."
        else:
            # Email not found
            return "Your email address is not in our database."
    except sqlite3.Error as error:
        return "An error occurred: " + str(error)
    finally:
        if conn:
            conn.close()

# Example usage
email = input("Enter your email to unsubscribe: ")
print(unsubscribe(email))