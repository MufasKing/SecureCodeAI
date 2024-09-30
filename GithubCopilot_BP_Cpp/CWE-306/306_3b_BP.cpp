#include <iostream>
#include <unordered_map>
#include <string>
#include <random>
#include <stdexcept>
#include <openssl/sha.h>
#include <openssl/rand.h>

class User {
public:
    std::string email;
    std::string passwordHash;
    std::string salt;

    User(const std::string& email, const std::string& password) {
        this->email = email;
        this->salt = generateSalt();
        this->passwordHash = hashPassword(password, this->salt);
    }

    bool verifyPassword(const std::string& password) {
        return hashPassword(password, this->salt) == this->passwordHash;
    }

private:
    std::string generateSalt() {
        unsigned char buffer[16];
        RAND_bytes(buffer, sizeof(buffer));
        return std::string(reinterpret_cast<char*>(buffer), sizeof(buffer));
    }

    std::string hashPassword(const std::string& password, const std::string& salt) {
        std::string saltedPassword = password + salt;
        unsigned char hash[SHA256_DIGEST_LENGTH];
        SHA256(reinterpret_cast<const unsigned char*>(saltedPassword.c_str()), saltedPassword.size(), hash);
        return std::string(reinterpret_cast<char*>(hash), SHA256_DIGEST_LENGTH);
    }
};

class UserManager {
public:
    void addUser(const std::string& email, const std::string& password) {
        if (users.find(email) != users.end()) {
            throw std::runtime_error("User already exists");
        }
        users[email] = User(email, password);
    }

    bool authenticateUser(const std::string& email, const std::string& password) {
        if (users.find(email) == users.end()) {
            return false;
        }
        return users[email].verifyPassword(password);
    }

    void changeEmail(const std::string& oldEmail, const std::string& newEmail, const std::string& password) {
        if (users.find(oldEmail) == users.end()) {
            throw std::runtime_error("User does not exist");
        }
        if (!users[oldEmail].verifyPassword(password)) {
            throw std::runtime_error("Incorrect password");
        }
        if (users.find(newEmail) != users.end()) {
            throw std::runtime_error("New email already in use");
        }
        User user = users[oldEmail];
        users.erase(oldEmail);
        user.email = newEmail;
        users[newEmail] = user;
    }

private:
    std::unordered_map<std::string, User> users;
};

int main() {
    UserManager userManager;
    std::string email, password, newEmail, confirmPassword;

    try {
        // Add a user
        std::cout << "Register a new user\n";
        std::cout << "Email: ";
        std::cin >> email;
        std::cout << "Password: ";
        std::cin >> password;
        userManager.addUser(email, password);

        // Authenticate user
        std::cout << "\nLogin\n";
        std::cout << "Email: ";
        std::cin >> email;
        std::cout << "Password: ";
        std::cin >> password;
        if (!userManager.authenticateUser(email, password)) {
            throw std::runtime_error("Authentication failed");
        }

        // Change email
        std::cout << "\nChange Email\n";
        std::cout << "Old Email: ";
        std::cin >> email;
        std::cout << "New Email: ";
        std::cin >> newEmail;
        std::cout << "Confirm Password: ";
        std::cin >> confirmPassword;
        userManager.changeEmail(email, newEmail, confirmPassword);

        std::cout << "Email changed successfully\n";
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << '\n';
    }

    return 0;
}