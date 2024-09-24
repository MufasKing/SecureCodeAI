#include <iostream>
#include <string>
#include <sqlite3.h>
#include <bcrypt/BCrypt.hpp>

// Function to open the database
sqlite3* openDatabase(const char* filename) {
    sqlite3* db;
    int exit = sqlite3_open(filename, &db);
    if (exit) {
        std::cerr << "Error opening database: " << sqlite3_errmsg(db) << std::endl;
        return nullptr;
    }
    return db;
}

// Function to check if a username already exists in the database
bool usernameExists(sqlite3* db, const std::string& username) {
    std::string query = "SELECT COUNT(*) FROM users WHERE username = ?;";
    sqlite3_stmt* stmt;
    sqlite3_prepare_v2(db, query.c_str(), -1, &stmt, nullptr);
    sqlite3_bind_text(stmt, 1, username.c_str(), -1, SQLITE_STATIC);
    
    int result = sqlite3_step(stmt);
    int count = 0;
    if (result == SQLITE_ROW) {
        count = sqlite3_column_int(stmt, 0);
    }
    sqlite3_finalize(stmt);
    
    return count > 0;
}

// Function to insert the user into the database
bool insertUser(sqlite3* db, const std::string& username, const std::string& passwordHash, const std::string& firstName, const std::string& lastName, const std::string& email) {
    std::string query = "INSERT INTO users (username, password, first_name, last_name, email) VALUES (?, ?, ?, ?, ?);";
    sqlite3_stmt* stmt;
    sqlite3_prepare_v2(db, query.c_str(), -1, &stmt, nullptr);
    
    sqlite3_bind_text(stmt, 1, username.c_str(), -1, SQLITE_STATIC);
    sqlite3_bind_text(stmt, 2, passwordHash.c_str(), -1, SQLITE_STATIC);
    sqlite3_bind_text(stmt, 3, firstName.c_str(), -1, SQLITE_STATIC);
    sqlite3_bind_text(stmt, 4, lastName.c_str(), -1, SQLITE_STATIC);
    sqlite3_bind_text(stmt, 5, email.c_str(), -1, SQLITE_STATIC);
    
    if (sqlite3_step(stmt) != SQLITE_DONE) {
        std::cerr << "Error inserting user: " << sqlite3_errmsg(db) << std::endl;
        sqlite3_finalize(stmt);
        return false;
    }
    sqlite3_finalize(stmt);
    return true;
}

// Function to register a user
void registerUser(sqlite3* db) {
    std::string username, password, firstName, lastName, email;
    
    std::cout << "Enter Username: ";
    std::cin >> username;
    std::cout << "Enter Password: ";
    std::cin >> password;
    std::cout << "Enter First Name: ";
    std::cin >> firstName;
    std::cout << "Enter Last Name: ";
    std::cin >> lastName;
    std::cout << "Enter Email: ";
    std::cin >> email;

    // Check if the username already exists
    if (usernameExists(db, username)) {
        std::cout << "Username already exists!" << std::endl;
        return;
    }

    // Hash the password using bcrypt
    std::string passwordHash = BCrypt::generateHash(password);
    
    // Insert the user into the database
    if (insertUser(db, username, passwordHash, firstName, lastName, email)) {
        std::cout << "Registration succeeded!" << std::endl;
    } else {
        std::cout << "Registration failed!" << std::endl;
    }
}

// Function to create the users table if it doesn't exist
void createUsersTable(sqlite3* db) {
    std::string query = 
        "CREATE TABLE IF NOT EXISTS users ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "username TEXT UNIQUE, "
        "password TEXT, "
        "first_name TEXT, "
        "last_name TEXT, "
        "email TEXT);";
        
    char* errMsg;
    if (sqlite3_exec(db, query.c_str(), 0, 0, &errMsg) != SQLITE_OK) {
        std::cerr << "Error creating table: " << errMsg << std::endl;
        sqlite3_free(errMsg);
    }
}

int main() {
    sqlite3* db = openDatabase("users.db");
    if (!db) {
        return -1;
    }
    
    createUsersTable(db);
    
    char option;
    do {
        std::cout << "Register a new user? (y/n): ";
        std::cin >> option;
        if (option == 'y') {
            registerUser(db);
        }
    } while (option != 'n');
    
    sqlite3_close(db);
    return 0;
}
