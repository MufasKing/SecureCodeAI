class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class SimpleLoginSystem:
    def __init__(self):
        self.users = {}  # This will hold users with username as key

    def register_user(self, username, password, email):
        if username in self.users:
            print("Username already exists.")
        else:
            self.users[username] = User(username, password, email)
            print("User registered successfully.")

    def login(self, username, password):
        if username in self.users and self.users[username].password == password:
            print("Login successful.")
            return True
        else:
            print("Login failed. Incorrect username or password.")
            return False

    def change_email(self, username, old_email, new_email, password):
        user = self.users.get(username)
        if user:
            if user.email == old_email and user.password == password:
                user.email = new_email
                print("Email changed successfully.")
            else:
                print("Failed to change email. Incorrect old email or password.")
        else:
            print("User not found.")

# Example Usage
def main():
    system = SimpleLoginSystem()
    
    # Register a user
    system.register_user("john_doe", "password123", "john@example.com")

    # Login
    if system.login("john_doe", "password123"):
        # Change email
        system.change_email("john_doe", "john@example.com", "john.new@example.com", "password123")
        
        # Attempting to change email with incorrect credentials
        system.change_email("john_doe", "john@example.com", "john.wrong@example.com", "wrongpassword")

if __name__ == "__main__":
    main()
