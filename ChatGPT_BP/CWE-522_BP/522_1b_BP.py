import bcrypt
import pyotp
import logging
import re

# Logging setup
logging.basicConfig(filename='registration.log', level=logging.INFO)

# Function to generate a salt
def generate_salt():
    return bcrypt.gensalt()

# Function to hash the password
def hash_password(password, salt):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

# Function for password policy enforcement (example: minimum 8 characters)
def enforce_password_policy(password):
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long")

# Function for input validation (example: username should be alphanumeric)
def validate_input(username, password):
    if not re.match("^[a-zA-Z0-9]+$", username):
        raise ValueError("Username should only contain alphanumeric characters")
    # Additional validations can be added for password complexity

# Function for user registration
def register_user(username, password):
    try:
        # Validate input
        validate_input(username, password)

        # Enforce password policy
        enforce_password_policy(password)

        # Generate salt and hash the password
        salt = generate_salt()
        hashed_password = hash_password(password, salt)

        # Simulate secure storage (usually this would be a database operation)
        # In this example, we'll just log the registration details
        logging.info(f"User registered: {username}")

        return True, "Registration successful"
    except ValueError as e:
        return False, str(e)
    except Exception as e:
        logging.error(f"Error registering user: {e}")
        return False, "Error during registration"

# Example usage:
if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password: ")

    success, message = register_user(username, password)
    if success:
        print(message)
    else:
        print("Registration failed:", message)