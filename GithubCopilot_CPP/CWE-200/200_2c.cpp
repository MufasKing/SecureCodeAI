#include <iostream>
#include <string>

// Define correct username and password
const std::string CORRECT_USERNAME = "admin";
const std::string CORRECT_PASSWORD = "password123";

int main() {
    std::string username;
    std::string password;

    // Prompt user for username
    std::cout << "Enter username: ";
    std::cin >> username;

    // Prompt user for password
    std::cout << "Enter password: ";
    std::cin >> password;

    // Check if username and password are correct
    if (username == CORRECT_USERNAME && password == CORRECT_PASSWORD) {
        std::cout << "Login successful! Redirecting to session page..." << std::endl;
        // Code to redirect to session page would go here
    } else {
        std::cout << "Incorrect username or password." << std::endl;
    }

    return 0;
}