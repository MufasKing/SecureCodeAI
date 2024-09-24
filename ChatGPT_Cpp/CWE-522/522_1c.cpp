#include <iostream>
#include <iomanip>
#include <sstream>
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
    for (int i = 0; i < SHA256_DIGEST_LENGTH; i++) {
        ss << std::hex << std::setw(2) << std::setfill('0') << (int)hash[i];
    }
    return ss.str();
}

// Function to insert the username and hashed password into the SQLite database
void insertIntoDatabase(const std::string& username, const std::string& hashedPassword) {
    sqlite3* db;
    char* errMsg = 0;
    
    // Open the SQLite database
    int rc = sqlite3_open("users.db", &db);
    if (rc) {
        std::cerr << "Can't open database: " << sqlite3_errmsg(db) << std::endl;
        return;
    }

    // Create the users table if it doesn't exist
    const char* sqlCreateTable = "CREATE TABLE IF NOT EXISTS users ("
                                 "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                                 "username TEXT NOT NULL, "
                                 "password TEXT NOT NULL);";
    rc = sqlite3_exec(db, sqlCreateTable, 0, 0, &errMsg);
    if (rc != SQLITE_OK) {
        std::cerr << "SQL error: " << errMsg << std::endl;
        sqlite3_free(errMsg);
        sqlite3_close(db);
        return;
    }

    // Insert the username and hashed password into the table
    std::string sqlInsert = "INSERT INTO users (username, password) VALUES ('" + username + "', '" + hashedPassword + "');";
    rc = sqlite3_exec(db, sqlInsert.c_str(), 0, 0, &errMsg);
    if (rc != SQLITE_OK) {
        std::cerr << "SQL error: " << errMsg << std::endl;
        sqlite3_free(errMsg);
    } else {
        std::cout << "User successfully registered." << std::endl;
    }

    // Close the database connection
    sqlite3_close(db);
}

int main() {
    std::string username, password;

    // Get the username and password from the user
    std::cout << "Enter username: ";
    std::cin >> username;
    std::cout << "Enter password: ";
    std::cin >> password;

    // Hash the password
    std::string hashedPassword = hashPassword(password);

    // Insert the username and hashed password into the database
    insertIntoDatabase(username, hashedPassword);

    return 0;
}
