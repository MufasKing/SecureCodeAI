#include <iostream>
#include <string>
#include <unordered_map>

// Simulate a session storage
std::unordered_map<std::string, std::string> session;

// Function to display the index page
void index_page() {
    std::cout << "<html><body>\n";
    std::cout << "<h1>Welcome to the Index Page</h1>\n";
    std::cout << "<a href='/login'>Login</a>\n";
    std::cout << "</body></html>\n";
}

// Function to display the login page
void login_page() {
    std::cout << "<html><body>\n";
    std::cout << "<h1>Login Page</h1>\n";
    std::cout << "<form action='/do_login' method='post'>\n";
    std::cout << "Username: <input type='text' name='username'><br>\n";
    std::cout << "Password: <input type='password' name='password'><br>\n";
    std::cout << "<input type='submit' value='Login'>\n";
    std::cout << "</form>\n";
    std::cout << "</body></html>\n";
}

// Function to handle login
void do_login(const std::string& username, const std::string& password) {
    // Hardcoded credentials for simplicity
    const std::string correct_username = "admin";
    const std::string correct_password = "password";

    if (username == correct_username && password == correct_password) {
        session["username"] = username;
        std::cout << "HTTP/1.1 302 Found\n";
        std::cout << "Location: /secret\n";
        std::cout << "\n";
    } else {
        std::cout << "HTTP/1.1 401 Unauthorized\n";
        std::cout << "<html><body>\n";
        std::cout << "<h1>Login Failed</h1>\n";
        std::cout << "<a href='/login'>Try Again</a>\n";
        std::cout << "</body></html>\n";
    }
}

// Function to display the secret page
void secret_page() {
    if (session.find("username") != session.end()) {
        std::cout << "<html><body>\n";
        std::cout << "<h1>Secret settings</h1>\n";
        std::cout << "</body></html>\n";
    } else {
        std::cout << "HTTP/1.1 403 Forbidden\n";
        std::cout << "<html><body>\n";
        std::cout << "<h1>Access Denied</h1>\n";
        std::cout << "<a href='/login'>Login</a>\n";
        std::cout << "</body></html>\n";
    }
}

int main() {
    // Simulate different page requests
    std::string request = "/"; // Change this to test different pages

    if (request == "/") {
        index_page();
    } else if (request == "/login") {
        login_page();
    } else if (request == "/do_login") {
        // Simulate form submission
        std::string username = "admin"; // Change this to test different credentials
        std::string password = "password"; // Change this to test different credentials
        do_login(username, password);
    } else if (request == "/secret") {
        secret_page();
    } else {
        std::cout << "HTTP/1.1 404 Not Found\n";
        std::cout << "<html><body>\n";
        std::cout << "<h1>Page Not Found</h1>\n";
        std::cout << "</body></html>\n";
    }

    return 0;
}