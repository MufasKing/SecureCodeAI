class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def verify_credentials(self, email, password):
        return self.email == email and self.password == password

    def change_email(self, old_email, new_email, confirm_password):
        if self.verify_credentials(old_email, confirm_password):
            self.email = new_email
            return "Email changed successfully."
        else:
            return "Invalid credentials. Email not changed."

# Example usage
def main():
    # Create a user with an initial email and password
    user = User("user@example.com", "securepassword")

    # Simulate user input
    old_email = input("Enter your old email: ")
    new_email = input("Enter your new email: ")
    confirm_password = input("Enter your password to confirm: ")

    # Attempt to change the email
    result = user.change_email(old_email, new_email, confirm_password)
    print(result)

if __name__ == "__main__":
    main()