import sqlite3
import requests
from urllib.parse import urlencode

# Database connection
DATABASE = 'emails.db'

def check_email_exists(email):
    # Input sanitization
    email = email.strip()
    
    # Check if the email exists in the database
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    query = "SELECT COUNT(*) FROM subscribers WHERE email = ?"
    cursor.execute(query, (email,))
    exists = cursor.fetchone()[0]
    conn.close()
    return exists > 0

def unsubscribe_email(email):
    # Secure URL construction
    base_url = "https://example.com/unsubscribe.php"
    params = {'email': email}
    url = f"{base_url}?{urlencode(params)}"
    
    # Secure HTTP Request
    try:
        response = requests.get(url)
        if response.status_code == 200:
            if response.text.strip() == '0':
                return 1
            else:
                return 0
        else:
            return 0
    except requests.RequestException as e:
        print(f"HTTP Request failed: {e}")
        return 0

def main(email):
    if check_email_exists(email):
        return unsubscribe_email(email)
    else:
        return 0

if __name__ == "__main__":
    email_to_check = input("Enter the email to unsubscribe: ")
    result = main(email_to_check)
    print(f"Result: {result}")