#include <iostream>
#include <sqlite3.h>     // SQLite library
#include <bcrypt/BCrypt.hpp>  // Assuming bcrypt-cpp is installed
#include <string>

// Function to create the users table if it doesn't exist
void createTable(sqlite3* db) {
    std::string sql = "CREATE TABLE IF NOT EXISTS users("
                      "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                      "username TEXT NOT NULL, "
                      "password TEXT NOT NULL);";
    char* errMsg = nullptr;
    int rc = sqlite3_exec(db, sql.c_str(), nullptr, nullptr, &errMsg);
    
    if (rc != SQLITE_OK) {
        std::cerr << "SQL error: " << errMsg << std::endl;
        sqlite3_free(errMsg);
    } else {
        std::cout << "Table created successfully or already exists." << std::endl;
    }
}

// Function to insert username and hashed password into the database
void insertUser(sqlite3* db, const std::string& username, const std::string& hashedPassword) {
    std::string sql = "INSERT INTO users(username, password) VALUES(?, ?);";
    sqlite3_stmt* stmt;
    
    if (sqlite3_prepare_v2(db, sql.c_str(), -1, &stmt, nullptr) != SQLITE_OK) {
        std::cerr << "Failed to prepare statement" << std::endl;
        return;
    }
    
    // Bind the username and hashed password
    sqlite3_bind_text(stmt, 1, username.c_str(), -1, SQLITE_STATIC);
    sqlite3_bind_text(stmt, 2, hashedPassword.c_str(), -1, SQLITE_STATIC);
    
    // Execute the SQL statement
    if (sqlite3_step(stmt) != SQLITE_DONE) {
        std::cerr << "Failed to insert data" << std::endl;
    } else {
        std::cout << "User added successfully." << std::endl;
    }

    sqlite3_finalize(stmt);
}

int main() {
    sqlite3* db;
    std::string dbName = "userdb.sqlite";

    // Open the database
    if (sqlite3_open(dbName.c_str(), &db) != SQLITE_OK) {
        std::cerr << "Can't open database: " << sqlite3_errmsg(db) << std::endl;
        return 1;
    }
    
    // Create users table if it doesn't exist
    createTable(db);
    
    // Get username and password input from the user
    std::string username, password;
    std::cout << "Enter username: ";
    std::getline(std::cin, username);
    std::cout << "Enter password: ";
    std::getline(std::cin, password);
    
    // Hash the password using bcrypt
    std::string hashedPassword = BCrypt::generateHash(password);
    
    // Insert the username and hashed password into the database
    insertUser(db, username, hashedPassword);
    
    // Close the database
    sqlite3_close(db);

    return 0;
}
