#include <iostream>
#include <string>

class User {
private:
    std::string username;
    std::string email;
    std::string password;
    bool loggedIn;

public:
    User(std::string u, std::string e, std::string p) : username(u), email(e), password(p), loggedIn(false) {}

    bool login(std::string u, std::string p) {
        if (username == u && password == p) {
            loggedIn = true;
            std::cout << "Login successful!" << std::endl;
            return true;
        } else {
            std::cout << "Login failed!" << std::endl;
            return false;
        }
    }

    bool changeEmail(std::string oldEmail, std::string newEmail, std::string p) {
        if (loggedIn && email == oldEmail && password == p) {
            email = newEmail;
            std::cout << "Email changed successfully!" << std::endl;
            return true;
        } else {
            std::cout << "Failed to change email. Please check your credentials." << std::endl;
            return false;
        }
    }

    void logout() {
        loggedIn = false;
        std::cout << "Logged out successfully!" << std::endl;
    }

    std::string getEmail() const {
        return email;
    }
};

int main() {
    User user("john_doe", "john@example.com", "password123");

    // Attempt to login
    user.login("john_doe", "password123");

    // Attempt to change email
    user.changeEmail("john@example.com", "john_new@example.com", "password123");

    // Display the new email
    std::cout << "New email: " << user.getEmail() << std::endl;

    // Logout
    user.logout();

    return 0;
}