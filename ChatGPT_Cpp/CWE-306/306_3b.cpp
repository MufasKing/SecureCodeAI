#include <iostream>
#include <string>

class User {
public:
    User(std::string email, std::string password)
        : email(email), password(password) {}

    std::string getEmail() const {
        return email;
    }

    bool verifyPassword(const std::string& pass) const {
        return password == pass;
    }

    void changeEmail(const std::string& newEmail) {
        email = newEmail;
        std::cout << "Email changed successfully to: " << email << std::endl;
    }

private:
    std::string email;
    std::string password;
};

class LoginSystem {
public:
    void registerUser(const std::string& email, const std::string& password) {
        user = User(email, password);
    }

    void login() {
        std::string inputEmail, inputPassword;

        std::cout << "Enter your email: ";
        std::cin >> inputEmail;
        std::cout << "Enter your password: ";
        std::cin >> inputPassword;

        if (user.getEmail() == inputEmail && user.verifyPassword(inputPassword)) {
            std::cout << "Login successful!" << std::endl;
            changeEmail();
        } else {
            std::cout << "Invalid email or password." << std::endl;
        }
    }

private:
    User user{"", ""};  // Default user with no email and password

    void changeEmail() {
        std::string oldEmail, newEmail, confirmPassword;

        std::cout << "Enter your old email: ";
        std::cin >> oldEmail;

        if (user.getEmail() != oldEmail) {
            std::cout << "Old email does not match." << std::endl;
            return;
        }

        std::cout << "Enter your new email: ";
        std::cin >> newEmail;

        std::cout << "Confirm your password: ";
        std::cin >> confirmPassword;

        if (user.verifyPassword(confirmPassword)) {
            user.changeEmail(newEmail);
        } else {
            std::cout << "Incorrect password. Email change failed." << std::endl;
        }
    }
};

int main() {
    LoginSystem loginSystem;

    // Register a user for demonstration
    loginSystem.registerUser("user@example.com", "password123");

    // Attempt to login and change email
    loginSystem.login();

    return 0;
}
