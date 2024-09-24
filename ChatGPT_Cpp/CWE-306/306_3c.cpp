#include <iostream>
#include <string>

class User {
public:
    User(const std::string& email, const std::string& password)
        : email(email), password(password), loggedIn(false) {}

    bool login(const std::string& inputEmail, const std::string& inputPassword) {
        if (inputEmail == email && inputPassword == password) {
            loggedIn = true;
            std::cout << "Login successful!\n";
            return true;
        } else {
            std::cout << "Invalid email or password.\n";
            return false;
        }
    }

    void changeEmail(const std::string& oldEmail, const std::string& inputPassword, const std::string& newEmail) {
        if (loggedIn) {
            if (oldEmail == email && inputPassword == password) {
                email = newEmail;
                std::cout << "Email changed successfully to: " << email << "\n";
            } else {
                std::cout << "Error: Incorrect old email or password. Email not changed.\n";
            }
        } else {
            std::cout << "Error: You must be logged in to change your email.\n";
        }
    }

private:
    std::string email;
    std::string password;
    bool loggedIn;
};

int main() {
    std::string email, password;
    
    // Initialize a user with a predefined email and password
    User user("user@example.com", "securepassword");

    // Simulate user login
    std::cout << "Enter your email: ";
    std::getline(std::cin, email);
    std::cout << "Enter your password: ";
    std::getline(std::cin, password);
    
    if (user.login(email, password)) {
        // If login is successful, allow email change
        std::string oldEmail, newEmail;
        std::cout << "Enter your old email: ";
        std::getline(std::cin, oldEmail);
        std::cout << "Enter your password again for confirmation: ";
        std::getline(std::cin, password);
        std::cout << "Enter your new email: ";
        std::getline(std::cin, newEmail);

        user.changeEmail(oldEmail, password, newEmail);
    }

    return 0;
}
