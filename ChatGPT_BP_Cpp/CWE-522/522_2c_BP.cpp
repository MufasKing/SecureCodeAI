#include <iostream>
#include <string>
#include <sstream>
#include <iomanip>
#include <openssl/sha.h>
#include <random>
#include <vector>

// Function to generate a random salt
std::string generateSalt(size_t length) {
    std::random_device rd;  // Obtain a random number from hardware
    std::mt19937 eng(rd()); // Seed the generator
    std::uniform_int_distribution<> distr(0, 255); // Define the range

    std::vector<unsigned char> salt(length);
    for (size_t i = 0; i < length; ++i) {
        salt[i] = static_cast<unsigned char>(distr(eng));
    }

    std::ostringstream oss;
    for (unsigned char byte : salt) {
        oss << std::hex << std::setw(2) << std::setfill('0') << static_cast<int>(byte);
    }
    return oss.str();
}

// Function to hash a password with SHA-256
std::string hashPassword(const std::string& password) {
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256(reinterpret_cast<const unsigned char*>(password.c_str()), password.size(), hash);

    std::ostringstream oss;
    for (unsigned char byte : hash) {
        oss << std::hex << std::setw(2) << std::setfill('0') << static_cast<int>(byte);
    }
    return oss.str();
}

// Function to register a user
void registerUser() {
    std::string username;
    std::string password;

    // Get username and password from user
    std::cout << "Enter username: ";
    std::getline(std::cin, username);
    std::cout << "Enter password: ";
    std::getline(std::cin, password);

    // Generate a random salt
    std::string salt = generateSalt(16); // Generate 16-byte salt

    // Hash the password
    std::string hashedPassword = hashPassword(password);

    // Concatenate salt and hashed password
    std::string storedValue = salt + ":" + hashedPassword;

    // Simulating database storage by printing to console
    std::cout << "Stored in database: " << storedValue << std::endl;
}

int main() {
    registerUser();
    return 0;
}
