#include <iostream>
#include <string>
#include <unordered_map>

class LoginSystem {
public:
    LoginSystem() {
        // Simulating a simple user database with username and password
        users["admin"] = "password123";  // Example user
    }

    bool login(const std::string& username, const std::string& password) {
        // Check if username exists and password matches
        auto it = users.find(username);
        if (it != users.end() && it->second == password) {
            return true; // Login successful
        }
        return false; // Login failed
    }

private:
    std::unordered_map<std::string, std::string> users; // Simulated database
};

int main() {
    LoginSystem loginSystem;
    std::string username, password;

    std::cout << "Enter username: ";
    std::getline(std::cin, username);
    std::cout << "Enter password: ";
    std::getline(std::cin, password);

    // Attempt to login
    if (loginSystem.login(username, password)) {
        std::cout << "Login successful! Redirecting to home page..." << std::endl;
        // Here you would typically redirect to the home page
    } else {
        std::cout << "Login failed! Redirecting to login page..." << std::endl;
        // Here you would typically redirect back to the login page
    }

    return 0;
}
