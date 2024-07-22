import bcrypt

def register_user():
    # Get username and password from the user
    username = input("Enter username: ")
    password = input("Enter password: ").encode('utf-8')  # Encode password to bytes

    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password, salt)

    # In a real application, you'd store these in a database
    # For demonstration, we will just print them
    print(f"Username: {username}")
    print(f"Hashed Password: {hashed_password.decode('utf-8')}")

if __name__ == "__main__":
    register_user()
