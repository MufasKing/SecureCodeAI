# Simple database structure
database = {
    'user1': 'password1',
    'user2': 'password2',
    'user3': 'password3'
}

def check_login(username, password):
    """
    Check if the provided username and password match the database.
    """
    if username in database and database[username] == password:
        return True
    return False

def login(username, password):
    """
    Handle the login process.
    """
    if check_login(username, password):
        print("Login successful! Redirecting to dashboard...")
        redirect_to_dashboard()
    else:
        print("Login failed! Redirecting back to login page...")
        redirect_to_login()

def redirect_to_dashboard():
    """
    Simulate redirecting to the dashboard page.
    """
    print("Welcome to the dashboard!")

def redirect_to_login():
    """
    Simulate redirecting back to the login page.
    """
    print("Please try logging in again.")

# Example usage
username = input("Enter username: ")
password = input("Enter password: ")
login(username, password)