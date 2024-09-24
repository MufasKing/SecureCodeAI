#include <iostream>
#include <string>
#include <unordered_map>

// Mock database for demonstration purposes
std::unordered_map<std::string, std::string> mockDatabase = {
    {"user1", "password1"},
    {"user2", "password2"}
};

// Function to simulate querying the database for a username
bool usernameExists(const std::string& username) {
    return mockDatabase.find(username) != mockDatabase.end();
}

// Function to check the password for the given username
bool checkPassword(const std::string& username, const std::string& password) {
    return mockDatabase[username] == password;
}

// Login function that checks username and password
void login(const std::string& username, const std::string& password) {
    if (!usernameExists(username)) {
        std::cout << "Username does not exist." << std::endl;
        return;
    }

    if (checkPassword(username, password)) {
        std::cout << "Login successful! Redirecting to home page..." << std::endl;
        // Here you would redirect to the home page in a real application
    } else {
        std::cout << "Incorrect password." << std::endl;
    }
}

int main() {
    std::string username;
    std::string password;

    // User input
    std::cout << "Enter username: ";
    std::cin >> username;
    std::cout << "Enter password: ";
    std::cin >> password;

    // Call login function
    login(username, password);

    return 0;
}
