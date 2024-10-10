#include <iostream>
#include <string>

bool checkCredentials(const std::string& username, const std::string& password) {
    // Simulated database credentials
    const std::string correctUsername = "admin";
    const std::string correctPassword = "password123";

    return (username == correctUsername && password == correctPassword);
}

void redirectToDashboard() {
    std::cout << "Redirecting to dashboard..." << std::endl;
    // Code to redirect to dashboard
}

void redirectToLoginPage() {
    std::cout << "Redirecting to login page..." << std::endl;
    // Code to redirect to login page
}

int main() {
    std::string username;
    std::string password;

    // Prompt user for username and password
    std::cout << "Enter username: ";
    std::cin >> username;
    std::cout << "Enter password: ";
    std::cin >> password;

    // Check credentials
    if (checkCredentials(username, password)) {
        std::cout << "Login successful!" << std::endl;
        redirectToDashboard();
    } else {
        std::cout << "Login failed!" << std::endl;
        redirectToLoginPage();
    }

    return 0;
}