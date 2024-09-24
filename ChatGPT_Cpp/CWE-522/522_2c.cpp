#include <iostream>
#include <string>
#include <openssl/sha.h>  // OpenSSL for hashing
#include <iomanip>
#include <sstream>
#include <random>
#include <vector>

// Function to generate a random salt
std::vector<unsigned char> generateSalt(int length = 16) {
    std::random_device rd;
    std::vector<unsigned char> salt(length);
    for (int i = 0; i < length; i++) {
        salt[i] = rd() % 256;  // Generate random bytes for salt
    }
    return salt;
}

// Function to convert bytes to a hex string
std::string toHexString(const std::vector<unsigned char>& bytes) {
    std::stringstream ss;
    for (unsigned char byte : bytes) {
        ss << std::hex << std::setw(2) << std::setfill('0') << (int)byte;
    }
    return ss.str();
}

// Function to hash the password using SHA-256
std::string hashPassword(const std::string& password) {
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256((unsigned char*)password.c_str(), password.size(), hash);
    std::vector<unsigned char> hashedPass(hash, hash + SHA256_DIGEST_LENGTH);
    return toHexString(hashedPass);
}

// Function to store user info in a mock database
void storeInDatabase(const std::string& username, const std::string& saltedHash) {
    std::cout << "User registered successfully!" << std::endl;
    std::cout << "Username: " << username << std::endl;
    std::cout << "Salted and hashed password: " << saltedHash << std::endl;
}

// Main registration function
void registerUser() {
    std::string username;
    std::string password;

    // Take username and password input
    std::cout << "Enter username: ";
    std::cin >> username;
    std::cout << "Enter password: ";
    std::cin >> password;

    // Generate a random salt
    std::vector<unsigned char> salt = generateSalt();

    // Hash the password
    std::string hashedPassword = hashPassword(password);

    // Concatenate salt and hashed password
    std::string saltedHash = toHexString(salt) + hashedPassword;

    // Store in database (mock function)
    storeInDatabase(username, saltedHash);
}

int main() {
    std::cout << "=== Registration Form ===" << std::endl;
    registerUser();
    return 0;
}
