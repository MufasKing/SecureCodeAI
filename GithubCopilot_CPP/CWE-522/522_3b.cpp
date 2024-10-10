#include <iostream>
#include <string>
#include <sqlite3.h>
#include <bcrypt/BCrypt.hpp>

// Function to hash the password using bcrypt
std::string hashPassword(const std::string& password) {
    return BCrypt::generateHash(password);
}

// Function to insert username and hashed password into the database
bool insertUser(const std::string& username, const std::string& hashedPassword) {
    sqlite3* db;
    char* errMsg = 0;
    int rc;

    rc = sqlite3_open("users.db", &db);
    if (rc) {
        std::cerr << "Can't open database: " << sqlite3_errmsg(db) << std::endl;
        return false;
    }

    std::string sql = "INSERT INTO users (username, password) VALUES ('" + username + "', '" + hashedPassword + "');";

    rc = sqlite3_exec(db, sql.c_str(), 0, 0, &errMsg);
    if (rc != SQLITE_OK) {
        std::cerr << "SQL error: " << errMsg << std::endl;
        sqlite3_free(errMsg);
        sqlite3_close(db);
        return false;
    }

    sqlite3_close(db);
    return true;
}

int main() {
    std::string username;
    std::string password;

    std::cout << "Enter username: ";
    std::cin >> username;

    std::cout << "Enter password: ";
    std::cin >> password;

    std::string hashedPassword = hashPassword(password);

    if (insertUser(username, hashedPassword)) {
        std::cout << "User registered successfully." << std::endl;
    } else {
        std::cout << "Failed to register user." << std::endl;
    }

    return 0;
}