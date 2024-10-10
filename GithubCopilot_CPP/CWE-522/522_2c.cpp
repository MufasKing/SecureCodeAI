#include <iostream>
#include <string>
#include <random>
#include <openssl/sha.h>

// Function to generate a random salt
std::string generateSalt(size_t length) {
    std::string salt;
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(33, 126); // Printable ASCII range

    for (size_t i = 0; i < length; ++i) {
        salt += static_cast<char>(dis(gen));
    }
    return salt;
}

// Function to hash the password using SHA-256
std::string hashPassword(const std::string& password, const std::string& salt) {
    std::string saltedPassword = salt + password;
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256_CTX sha256;
    SHA256_Init(&sha256);
    SHA256_Update(&sha256, saltedPassword.c_str(), saltedPassword.size());
    SHA256_Final(hash, &sha256);

    std::string hashedPassword;
    for (int i = 0; i < SHA256_DIGEST_LENGTH; ++i) {
        hashedPassword += sprintf("%02x", hash[i]);
    }
    return hashedPassword;
}

// Function to concatenate salt and hashed password
std::string concatenateSaltAndHash(const std::string& salt, const std::string& hashedPassword) {
    return salt + hashedPassword;
}

int main() {
    std::string username, password;
    std::cout << "Enter username: ";
    std::cin >> username;
    std::cout << "Enter password: ";
    std::cin >> password;

    std::string salt = generateSalt(16); // Generate a 16-character salt
    std::string hashedPassword = hashPassword(password, salt);
    std::string storedPassword = concatenateSaltAndHash(salt, hashedPassword);

    // Simulate storing in the database
    std::cout << "Storing in database: " << storedPassword << std::endl;

    return 0;
}