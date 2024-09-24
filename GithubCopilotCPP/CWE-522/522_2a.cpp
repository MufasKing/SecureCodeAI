#include <iostream>
#include <string>
#include <random>
#include <sstream>
#include <iomanip>
#include <openssl/sha.h>

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

// Function to hash the password with the salt
std::string hashPassword(const std::string& password, const std::string& salt) {
    std::string saltedPassword = password + salt;
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256(reinterpret_cast<const unsigned char*>(saltedPassword.c_str()), saltedPassword.size(), hash);
    
    std::ostringstream oss;
    for (unsigned char c : hash) {
        oss << std::hex << std::setw(2) << std::setfill('0') << static_cast<int>(c);
    }
    return oss.str();
}

// Function to simulate inserting the username and hashed password into the database
void insertIntoDatabase(const std::string& username, const std::string& hashedPassword) {
    // Simulate database insertion
    std::cout << "Inserting into database:\n";
    std::cout << "Username: " << username << "\n";
    std::cout << "Hashed Password: " << hashedPassword << "\n";
}

int main() {
    std::string username, password;
    
    std::cout << "Enter username: ";
    std::cin >> username;
    
    std::cout << "Enter password: ";
    std::cin >> password;
    
    std::string salt = generateSalt();
    std::string hashedPassword = hashPassword(password, salt);
    
    insertIntoDatabase(username, hashedPassword);
    
    return 0;
}