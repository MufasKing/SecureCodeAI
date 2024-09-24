#include <iostream>
#include <string>

class LoginSystem {
private:
    std::string storedUsername = "admin";   // Simulated stored username
    std::string storedPassword = "password"; // Simulated stored password

public:
    void login() {
        std::string username;
        std::string password;

        std::cout << "Welcome to the Login Page!" << std::endl;

        // Taking input from the user
        std::cout << "Enter Username: ";
        std::cin >> username;
        std::cout << "Enter Password: ";
        std::cin >> password;

        // Checking credentials
        if (checkCredentials(username, password)) {
            redirectToDashboard();
        } else {
            redirectToLogin();
        }
    }

private:
    bool checkCredentials(const std::string& username, const std::string& password) {
        return (username == storedUsername && password == storedPassword);
    }

    void redirectToDashboard() {
        std::cout << "Login successful! Redirecting to the dashboard..." << std::endl;
        // Here you would implement the logic to show the dashboard
    }

    void redirectToLogin() {
        std::cout << "Invalid username or password. Redirecting back to the login page..." << std::endl;
        // Here you could loop back to the login function for another attempt if desired
        login(); // For demonstration, we call login() again
    }
};

int main() {
    LoginSystem app;
    app.login();
    return 0;
}
