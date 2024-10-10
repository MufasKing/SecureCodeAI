import hashlib
import secrets
import string
from hmac import compare_digest

# Assuming a simple form structure where data is collected
# This is a mock function to simulate form data collection
def get_form_data():
    # In a real scenario, this would fetch data from the form fields
    return {"username": "user_input_username", "password": "user_input_password"}

# Mock database of users for demonstration purposes
# In a real application, this would be a database query
# Passwords are stored as hashes for security
users_db = {
    "user1": hashlib.sha256("secure_password1".encode()).hexdigest(),
    "user2": hashlib.sha256("secure_password2".encode()).hexdigest(),
}

def check_mod():
    form_data = get_form_data()
    username = form_data["username"]
    password = form_data["password"]
    
    # Input Validation
    if not username.isalnum() or not 1 <= len(password) <= 50:
        return False
    
    # Secure Randomness for salt (not shown here but should be used in real password hashing)
    salt = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(16))
    
    # Password Hashing
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    
    # Check if the username exists in the database
    if username in users_db:
        # Constant-Time String Comparison to mitigate timing attacks
        if compare_digest(users_db[username], password_hash):
            return True
    
    return False