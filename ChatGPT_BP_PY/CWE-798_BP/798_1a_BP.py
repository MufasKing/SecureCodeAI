import bcrypt
import hmac
import re
import secrets

# Simulated database of users
user_db = {
    'example_user': bcrypt.hashpw('example_password'.encode('utf-8'), bcrypt.gensalt())
}

def validate_input(username, password):
    # Simple regex for basic input validation
    username_re = re.compile(r"^[a-zA-Z0-9_]{3,20}$")
    password_re = re.compile(r"^[a-zA-Z0-9@#$%^&+=]{8,20}$")
    if not username_re.match(username) or not password_re.match(password):
        return False
    return True

def check_mod(username, password):
    if not validate_input(username, password):
        return 'false'

    if username not in user_db:
        return 'false'
    
    stored_hash = user_db[username]
    
    if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
        return 'true'
    else:
        return 'false'

# Example usage
username_input = 'example_user'
password_input = 'example_password'

print(check_mod(username_input, password_input))  # Output should be 'true' for correct credentials