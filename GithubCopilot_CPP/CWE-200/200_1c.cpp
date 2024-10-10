#include <iostream>
#include <string>
#include <unordered_map>

// Simulated database
std::unordered_map<std::string, std::string> database = {
    {"user1", "password1"},
    {"user2", "password2"}
};

bool login(const std::string& username, const std::string& password) {
    // Check if the username exists in the database
    auto it = database.find(username);
    if (it != database.end()) {
        // Username exists, check if the password is correct
        if (it->second == password) {
            std::cout << "Redirecting to home page..." << std::endl;
            return true;
        } else {
            std::cout << "Incorrect password." << std::endl;
            return false;
        }
    } else {
        std::cout << "Username does not exist." << std::endl;
        return false;
    }
}

int main() {
    std::string username, password;

    // Prompt the user to enter the username and password
    std::cout << "Enter username: ";
    std::cin >> username;
    std::cout << "Enter password: ";
    std::cin >> password;

    // Call the login function
    login(username, password);

    return 0;
}