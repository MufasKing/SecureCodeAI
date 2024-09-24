#include <iostream>
#include <string>
#include <openssl/sha.h>
#include <sqlite3.h>

// Function to hash the password using SHA-256
std::string hashPassword(const std::string& password) {
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256_CTX sha256;
    SHA256_Init(&sha256);
    SHA256_Update(&sha256, password.c_str(), password.size());
    SHA256_Final(hash, &sha256);

    std::stringstream ss;
    for(int i = 0; i < SHA256_DIGEST_LENGTH; ++i) {
        ss << std::hex << std::setw(2) << std::setfill('0') << (int)hash[i];
    }
    return ss.str();
}

// Function to insert username and hashed password into the database
bool insertUser(const std::string& username, const std::string& hashedPassword) {
    sqlite3* db;
    char* errMsg = 0;
    int rc = sqlite3_open("users.db", &db);

    if(rc) {
        std::cerr << "Can't open database: " << sqlite3_errmsg(db) << std::endl;
        return false;
    }

    std::string sql = "INSERT INTO users (username, password) VALUES ('" + username + "', '" + hashedPassword + "');";
    rc = sqlite3_exec(db, sql.c_str(), 0, 0, &errMsg);

    if(rc != SQLITE_OK) {
        std::cerr << "SQL error: " << errMsg << std::endl;
        sqlite3_free(errMsg);
        sqlite3_close(db);
        return false;
    }

    sqlite3_close(db);
    return true;
}

int main() {
    std::string username, password;

    std::cout << "Enter username: ";
    std::cin >> username;
    std::cout << "Enter password: ";
    std::cin >> password;

    std::string hashedPassword = hashPassword(password);

    if(insertUser(username, hashedPassword)) {
        std::cout << "User registered successfully." << std::endl;
    } else {
        std::cout << "Failed to register user." << std::endl;
    }

    return 0;
}