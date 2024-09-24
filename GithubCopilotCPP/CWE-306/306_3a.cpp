#include <iostream>
#include <string>

class User {
private:
    std::string username;
    std::string email;
    std::string password;

public:
    User(std::string uname, std::string mail, std::string pass)
        : username(uname), email(mail), password(pass) {}

    bool login(const std::string& uname, const std::string& pass) {
        return (username == uname && password == pass);
    }

    bool changeEmail(const std::string& oldEmail, const std::string& newEmail, const std::string& confirmPassword) {
        if (email != oldEmail) {
            std::cout << "Old email does not match." << std::endl;
            return false;
        }
        if (password != confirmPassword) {
            std::cout << "Password is incorrect." << std::endl;
            return false;
        }
        if (oldEmail == newEmail) {
            std::cout << "New email must be different from the old email." << std::endl;
            return false;
        }
        email = newEmail;
        std::cout << "Email changed successfully." << std::endl;
        return true;
    }

    std::string getEmail() const {
        return email;
    }
};

int main() {
    User user("john_doe", "john@example.com", "password123");

    std::string username, password, oldEmail, newEmail, confirmPassword;

    std::cout << "Enter username: ";
    std::cin >> username;
    std::cout << "Enter password: ";
    std::cin >> password;

    if (user.login(username, password)) {
        std::cout << "Login successful." << std::endl;

        std::cout << "Enter old email: ";
        std::cin >> oldEmail;
        std::cout << "Enter new email: ";
        std::cin >> newEmail;
        std::cout << "Confirm password: ";
        std::cin >> confirmPassword;

        user.changeEmail(oldEmail, newEmail, confirmPassword);
    } else {
        std::cout << "Login failed. Incorrect username or password." << std::endl;
    }

    return 0;
}