#include <iostream>
#include <openssl/sha.h>
#include <iomanip>
#include <sstream>

// Function to hash the password using SHA-256
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

int main() {
    std::string username;
    std::string password;

    // Take input from the user
    std::cout << "Enter username: ";
    std::cin >> username;
    
    std::cout << "Enter password: ";
    std::cin >> password;

    // Hash the password
    std::string hashedPassword = hashPassword(password);

    // Output the username and hashed password
    std::cout << "\nUsername: " << username << std::endl;
    std::cout << "Hashed Password: " << hashedPassword << std::endl;

    return 0;
}
