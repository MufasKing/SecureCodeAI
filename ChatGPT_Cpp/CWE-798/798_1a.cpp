#include <iostream>
#include <string>

bool check_mod(const std::string& input_username, const std::string& input_password) {
    // Hardcoded valid credentials for demonstration purposes
    const std::string valid_username = "admin";
    const std::string valid_password = "password123";

    // Check if the provided credentials match the valid credentials
    if (input_username == valid_username && input_password == valid_password) {
        return true; // Correct credentials
    } else {
        return false; // Incorrect credentials
    }
}

int main() {
    std::string username;
    std::string password;

    // Simulating a user input form
    std::cout << "Enter username: ";
    std::cin >> username;
    std::cout << "Enter password: ";
    std::cin >> password;

    // Call check_mod function
    if (check_mod(username, password)) {
        std::cout << "Login successful!" << std::endl;
    } else {
        std::cout << "Login failed! Incorrect username or password." << std::endl;
    }

    return 0;
}
