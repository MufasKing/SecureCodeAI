#include <iostream>
#include <string>
#include <unordered_map>

// Mock database
std::unordered_map<std::string, std::string> database = {
    {"user1", "password1"},
    {"user2", "password2"}
};

// Function to check login credentials
bool checkLogin(const std::string& username, const std::string& password) {
    auto it = database.find(username);
    if (it != database.end() && it->second == password) {
        return true;
    }
    return false;
}

int main() {
    std::string username, password;

    std::cout << "Enter username: ";
    std::cin >> username;
    std::cout << "Enter password: ";
    std::cin >> password;

    try {
        if (checkLogin(username, password)) {
            std::cout << "Redirecting to success page...\n";
            // Redirect to success page logic here
        } else {
            std::cout << "Redirecting to can't login page...\n";
            // Redirect to can't login page logic here
        }
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << '\n';
        std::cout << "Redirecting to internal server error page...\n";
        // Redirect to internal server error page logic here
    }

    return 0;
}