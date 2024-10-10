#include <iostream>
#include <string>

class User {
private:
    std::string email;
    std::string password;

public:
    User(std::string email, std::string password) : email(email), password(password) {}

    bool login(std::string email, std::string password) {
        return this->email == email && this->password == password;
    }

    bool changeEmail(std::string oldEmail, std::string newEmail, std::string confirmPassword) {
        if (this->email == oldEmail && this->password == confirmPassword) {
            this->email = newEmail;
            return true;
        }
        return false;
    }

    std::string getEmail() {
        return email;
    }
};

int main() {
    User user("user@example.com", "password123");

    std::string email, password, oldEmail, newEmail, confirmPassword;

    std::cout << "Login\n";
    std::cout << "Email: ";
    std::cin >> email;
    std::cout << "Password: ";
    std::cin >> password;

    if (user.login(email, password)) {
        std::cout << "Login successful!\n";

        std::cout << "Change Email\n";
        std::cout << "Old Email: ";
        std::cin >> oldEmail;
        std::cout << "New Email: ";
        std::cin >> newEmail;
        std::cout << "Confirm Password: ";
        std::cin >> confirmPassword;

        if (user.changeEmail(oldEmail, newEmail, confirmPassword)) {
            std::cout << "Email changed successfully to " << user.getEmail() << "\n";
        } else {
            std::cout << "Failed to change email. Please check your inputs.\n";
        }
    } else {
        std::cout << "Login failed. Incorrect email or password.\n";
    }

    return 0;
}