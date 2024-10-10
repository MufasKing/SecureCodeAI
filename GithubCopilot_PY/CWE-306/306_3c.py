class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.logged_in = False

    def login(self, email, password):
        if self.email == email and self.password == password:
            self.logged_in = True
            print("Login successful.")
        else:
            print("Login failed. Incorrect email or password.")

    def change_email(self, old_email, password, new_email):
        if not self.logged_in:
            print("You must be logged in to change your email.")
            return

        if self.email == old_email and self.password == password:
            self.email = new_email
            print("Email changed successfully.")
        else:
            print("Email change failed. Incorrect old email or password.")

# Example usage
user = User("john_doe", "john@example.com", "securepassword")

# Attempt to change email without logging in
user.change_email("john@example.com", "securepassword", "john_new@example.com")

# Log in with correct credentials
user.login("john@example.com", "securepassword")

# Attempt to change email with correct old email and password
user.change_email("john@example.com", "securepassword", "john_new@example.com")

# Attempt to change email with incorrect old email
user.change_email("wrong@example.com", "securepassword", "john_newer@example.com")

# Attempt to change email with incorrect password
user.change_email("john_new@example.com", "wrongpassword", "john_newest@example.com")