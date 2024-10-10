#include <iostream>
#include <string>
#include <unordered_map>
#include <random>
#include <openssl/sha.h>

// Database simulation
std::unordered_map<std::string, std::pair<std::string, std::string>> database;

// Function to generate a random salt
std::string generateSalt(size_t length = 16) {
    const char charset[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    std::default_random_engine rng(std::random_device{}());
    std::uniform_int_distribution<> dist(0, sizeof(charset) - 2);
    std::string salt;
    for (size_t i = 0; i < length; ++i) {
        salt += charset[dist(rng)];
    }
    return salt;
}

// Function to hash the password
std::string hashPassword(const std::string& password, const std::string& salt) {
    std::string saltedPassword = password + salt;
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256(reinterpret_cast<const unsigned char*>(saltedPassword.c_str()), saltedPassword.size(), hash);
    std::string hashedPassword(hash, hash + SHA256_DIGEST_LENGTH);
    return hashedPassword;
}

// Function to register a user
void registerUser(const std::string& username, const std::string& password) {
    std::string salt = generateSalt();
    std::string hashedPassword = hashPassword(password, salt);
    database[username] = {hashedPassword, salt};
    std::cout << "User registered successfully.\n";
}

// Function to verify the password during login
bool verifyPassword(const std::string& username, const std::string& password) {
    if (database.find(username) == database.end()) {
        return false;
    }
    std::string storedHashedPassword = database[username].first;
    std::string storedSalt = database[username].second;
    std::string hashedPassword = hashPassword(password, storedSalt);
    return hashedPassword == storedHashedPassword;
}

int main() {
    int choice;
    std::string username, password;

    while (true) {
        std::cout << "1. Register\n2. Login\n3. Exit\nEnter your choice: ";
        std::cin >> choice;

        if (choice == 1) {
            std::cout << "Enter username: ";
            std::cin >> username;
            std::cout << "Enter password: ";
            std::cin >> password;
            registerUser(username, password);
        } else if (choice == 2) {
            std::cout << "Enter username: ";
            std::cin >> username;
            std::cout << "Enter password: ";
            std::cin >> password;
            if (verifyPassword(username, password)) {
                std::cout << "Login successful.\n";
            } else {
                std::cout << "Invalid username or password.\n";
            }
        } else if (choice == 3) {
            break;
        } else {
            std::cout << "Invalid choice. Please try again.\n";
        }
    }

    return 0;
}