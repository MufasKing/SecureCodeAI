import sqlite3

# Initialize the database and create the table (run this once)
def setup_database():
    conn = sqlite3.connect('subscribers.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subscribers (
            email TEXT PRIMARY KEY
        )
    ''')
    conn.commit()
    conn.close()

# Function to unsubscribe an email address
def unsubscribe(email):
    conn = sqlite3.connect('subscribers.db')
    cursor = conn.cursor()
    
    # Check if the email exists in the database
    cursor.execute('SELECT email FROM subscribers WHERE email = ?', (email,))
    result = cursor.fetchone()
    
    if result:
        # Email found, so delete it
        cursor.execute('DELETE FROM subscribers WHERE email = ?', (email,))
        conn.commit()
        print(f'The email address {email} has been successfully unsubscribed.')
    else:
        # Email not found
        print(f'The email address {email} was not found in the database.')
    
    conn.close()

# Example usage
if __name__ == "__main__":
    setup_database()  # Set up the database and table (only needed once)

    # Simulate user input
    email_to_unsubscribe = input("Enter your email address to unsubscribe: ")
    
    # Call the unsubscribe function
    unsubscribe(email_to_unsubscribe)
