#include <iostream>
#include <string>
#include <regex>
#include <openssl/sha.h>
#include <iomanip>
#include <sstream>

// Utility function to hash a password
std::string hashPassword(const std::string& password) {
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256_CTX sha256;
    SHA256_Init(&sha256);
    SHA256_Update(&sha256, password.c_str(), password.size());
    SHA256_Final(hash, &sha256);
    std::stringstream ss;
    for (int i = 0; i < SHA256_DIGEST_LENGTH; ++i) {
        ss << std::hex << std::setw(2) << std::setfill('0') << (int)hash[i];
    }
    return ss.str();
}

// Utility function to validate email format
bool validateEmail(const std::string& email) {
    const std::regex pattern(R"((\w+)(\.{1}\w+)*@(\w+)(\.\w{2,3})+)");
    return std::regex_match(email, pattern);
}

// Secure string comparison
bool secureCompare(const std::string& a, const std::string& b) {
    if (a.size() != b.size()) return false;
    volatile unsigned char result = 0;
    for (size_t i = 0; i < a.size(); ++i) {
        result |= a[i] ^ b[i];
    }
    return result == 0;
}

class User {
private:
    std::string username;
    std::string email;
    std::string hashedPassword;

public:
    User(const std::string& uname, const std::string& mail, const std::string& password)
        : username(uname), email(mail), hashedPassword(hashPassword(password)) {}

    bool login(const std::string& uname, const std::string& password) {
        return (username == uname && secureCompare(hashedPassword, hashPassword(password)));
    }

    bool changeEmail(const std::string& oldEmail, const std::string& newEmail, const std::string& password) {
        if (!secureCompare(email, oldEmail)) {
            std::cerr << "Old email does not match." << std::endl;
            return false;
        }
        if (!validateEmail(newEmail)) {
            std::cerr << "Invalid new email format." << std::endl;
            return false;
        }
        if (secureCompare(email, newEmail)) {
            std::cerr << "New email must be different from the old email." << std::endl;
            return false;
        }
        if (!secureCompare(hashedPassword, hashPassword(password))) {
            std::cerr << "Incorrect password." << std::endl;
            return false;
        }
        email = newEmail;
        return true;
    }

    std::string getEmail() const {
        return email;
    }
};

int main() {
    User user("john_doe", "john@example.com", "securepassword123");

    std::string username, password, oldEmail, newEmail, confirmPassword;

    std::cout << "Login\nUsername: ";
    std::cin >> username;
    std::cout << "Password: ";
    std::cin >> password;

    if (user.login(username, password)) {
        std::cout << "Login successful.\n";

        std::cout << "Enter old email: ";
        std::cin >> oldEmail;
        std::cout << "Enter new email: ";
        std::cin >> newEmail;
        std::cout << "Confirm password: ";
        std::cin >> confirmPassword;

        if (user.changeEmail(oldEmail, newEmail, confirmPassword)) {
            std::cout << "Email changed successfully to " << user.getEmail() << ".\n";
        } else {
            std::cerr << "Failed to change email.\n";
        }
    } else {
        std::cerr << "Login failed.\n";
    }

    return 0;
}