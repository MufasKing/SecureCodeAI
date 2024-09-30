#include <iostream>
#include <unordered_map>
#include <string>
#include <regex>
#include <openssl/sha.h>
#include <ctime>
#include <cstdlib>
#include <iomanip>

// Simulated session storage
std::unordered_map<std::string, std::string> session;

// Simulated user database with hashed passwords
std::unordered_map<std::string, std::string> user_db = {
    {"user1", "5e884898da28047151d0e56f8dc6292773603d0d6aabbddf8a6e0e4b0b8f1e5e"} // password: "password"
};

// Function to hash passwords
std::string hash_password(const std::string& password) {
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256_CTX sha256;
    SHA256_Init(&sha256);
    SHA256_Update(&sha256, password.c_str(), password.size());
    SHA256_Final(hash, &sha256);
    std::stringstream ss;
    for(int i = 0; i < SHA256_DIGEST_LENGTH; i++) {
        ss << std::hex << std::setw(2) << std::setfill('0') << (int)hash[i];
    }
    return ss.str();
}

// Function to validate input
bool validate_input(const std::string& input) {
    std::regex pattern("^[a-zA-Z0-9_]+$");
    return std::regex_match(input, pattern);
}

// Function to handle login
bool do_login(const std::string& username, const std::string& password) {
    if (!validate_input(username) || !validate_input(password)) {
        return false;
    }

    std::string hashed_password = hash_password(password);
    if (user_db.find(username) != user_db.end() && user_db[username] == hashed_password) {
        session["username"] = username;
        return true;
    }
    return false;
}

// Function to check if user is logged in
bool is_logged_in() {
    return session.find("username") != session.end();
}

// Function to display index page
void display_index_page() {
    std::cout << "<html><body><a href='/login'>Login</a></body></html>" << std::endl;
}

// Function to display login page
void display_login_page() {
    std::cout << "<html><body>"
              << "<form method='POST' action='/do_login'>"
              << "Username: <input type='text' name='username'><br>"
              << "Password: <input type='password' name='password'><br>"
              << "<input type='submit' value='Login'>"
              << "</form></body></html>" << std::endl;
}

// Function to display secret page
void display_secret_page() {
    if (is_logged_in()) {
        std::cout << "<html><body>Secret settings</body></html>" << std::endl;
    } else {
        std::cout << "<html><body>Access Denied</body></html>" << std::endl;
    }
}

int main() {
    // Simulate different pages
    display_index_page();
    display_login_page();
    if (do_login("user1", "password")) {
        display_secret_page();
    } else {
        std::cout << "Login failed" << std::endl;
    }
    return 0;
}