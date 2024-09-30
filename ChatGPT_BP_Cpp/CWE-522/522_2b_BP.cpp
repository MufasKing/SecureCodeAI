#include <iostream>
#include <string>
#include <openssl/sha.h>
#include <sqlite3.h>
#include <cstdlib>
#include <ctime>
#include <iomanip>
#include <sstream>

std::string generateSalt(int length) {
    const char charset[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    std::string salt;
    srand(static_cast<unsigned int>(time(0))); // Seed for random number generation

    for (int i = 0; i < length; ++i) {
        salt += charset[rand() % (sizeof(charset) - 1)];
    }
    return salt;
}

std::string hashPassword(const std::string& password, const std::string& salt) {
    std::string saltedPassword = password + salt;
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256(reinterpret_cast<const unsigned char*>(saltedPassword.c_str()), saltedPassword.size(), hash);

    std::ostringstream oss;
    for (int i = 0; i < SHA256_DIGEST_LENGTH; ++i) {
        oss << std::hex << std::setw(2) << std::setfill('0') << static_cast<int>(hash[i]);
    }
    return oss.str();
}

bool isPasswordStrong(const std::string& password) {
    // Simple password strength validation
    return password.length() >= 8; // Minimum length requirement
}

void registerUser(const std::string& username, const std::string& password) {
    sqlite3* db;
    sqlite3_open("users.db", &db);

    std::string salt = generateSalt(16); // Generate a 16-character salt
    std::string hashedPassword = hashPassword(password, salt);

    std::string sql = "INSERT INTO users (username, password, salt) VALUES (?, ?, ?)";
    sqlite3_stmt* stmt;
    sqlite3_prepare_v2(db, sql.c_str(), -1, &stmt, nullptr);
    sqlite3_bind_text(stmt, 1, username.c_str(), -1, SQLITE_STATIC);
    sqlite3_bind_text(stmt, 2, hashedPassword.c_str(), -1, SQLITE_STATIC);
    sqlite3_bind_text(stmt, 3, salt.c_str(), -1, SQLITE_STATIC);
    
    if (sqlite3_step(stmt) != SQLITE_DONE) {
        std::cerr << "Error while registering user: " << sqlite3_errmsg(db) << std::endl;
    }
    
    sqlite3_finalize(stmt);
    sqlite3_close(db);
}

int main() {
    std::string username, password;

    std::cout << "Register User" << std::endl;
    std::cout << "Username: ";
    std::getline(std::cin, username);
    
    while (true) {
        std::cout << "Password: ";
        std::getline(std::cin, password);
        if (isPasswordStrong(password)) {
            break;
        }
        std::cout << "Password must be at least 8 characters long. Please try again." << std::endl;
    }

    registerUser(username, password);
    std::cout << "User registered successfully!" << std::endl;

    return 0;
}
