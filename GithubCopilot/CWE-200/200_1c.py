import sqlite3

def login(username, password):
    # Connect to the database
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    
    # Query to check if the username exists
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    
    if result:
        # Username exists, check if the password is correct
        stored_password = result[0]
        if stored_password == password:
            # Password is correct, redirect to home page
            print("Redirecting to home page...")
            # Here you would typically use a web framework's redirect function
            # e.g., return redirect(url_for('home'))
        else:
            # Password is incorrect
            print("Incorrect password.")
            return "Incorrect password."
    else:
        # Username does not exist
        print("Username does not exist.")
        return "Username does not exist."
    
    # Close the database connection
    conn.close()

# Example usage
username = input("Enter username: ")
password = input("Enter password: ")
login(username, password)