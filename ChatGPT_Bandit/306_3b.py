import hashlib

# Simulated user database (in-memory for this example)
users_db = {
    "user@example.com": {
        "password": hashlib.sha256("password123".encode()).hexdigest()  # Hash of the password
    }
}

def hash_password(password):
    """Hash a password for storing."""
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate_user(email, password):
    """Check if the provided email and password match."""
    if email in users_db:
        return users_db[email]["password"] == hash_password(password)
    return False

def change_email(current_email, new_email, confirm_password):
    """Change the user's email if the confirm password is correct."""
    if current_email not in users_db:
        return "Current email does not exist."
    
    if not authenticate_user(current_email, confirm_password):
        return "Incorrect password."

    if new_email in users_db:
        return "New email is already in use."

    # Update the email in the database
    users_db[new_email] = users_db.pop(current_email)
    return f"Email successfully changed to {new_email}."

def main():
    """Main function to handle user input and email change."""
    print("Welcome to the Email Change System")
    
    # User input
    current_email = input("Enter your current email: ").strip()
    new_email = input("Enter your new email: ").strip()
    confirm_password = input("Enter your password to confirm: ").strip()
    
    result = change_email(current_email, new_email, confirm_password)
    print(result)

if __name__ == "__main__":
    main()
