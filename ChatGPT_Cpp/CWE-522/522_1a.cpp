#include <iostream>
#include <string>
#include <openssl/md5.h>  // For MD5 hashing
#include <sqlite3.h>      // For SQLite

// Function to generate MD5 hash of a given string
std::string md5Hash(const std::string& input) {
    unsigned char digest[MD5_DIGEST_LENGTH];
    MD5((unsigned char*)input.c_str(), input.size(), (unsigned char*)&digest);

    char md5String[33];  // MD5 generates a 32-character hex string
    for (int i = 0; i < 16; ++i) {
        sprintf(&md5String[i * 2], "%02x", (unsigned int)digest[i]);
    }
    return std::string(md5String);
}

// Function to open and initialize the SQLite database
sqlite3* openDatabase(const std::string& dbName) {
    sqlite3* db;
    int exit = sqlite3_open(dbName.c_str(), &db);
    if (exit) {
        std::cerr << "Error opening SQLite database: " << sqlite3_errmsg(db) << std::endl;
        return nullptr;
    }
    return db;
}

// Function to create the users table in the database (if not exists)
void createUsersTable(sqlite3* db) {
    const char* createTableSQL = 
        "CREATE TABLE IF NOT EXISTS users ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "username TEXT NOT NULL UNIQUE, "
        "password TEXT NOT NULL);";

    char* errorMessage;
    int exit = sqlite3_exec(db, createTableSQL, nullptr, nullptr, &errorMessage);
    if (exit != SQLITE_OK) {
        std::cerr << "Error creating table: " << errorMessage << std::endl;
        sqlite3_free(errorMessage);
    }
}

// Function to insert a new user into the database
void insertUser(sqlite3* db, const std::string& username, const std::string& hashedPassword) {
    const char* insertSQL = "INSERT INTO users (username, password) VALUES (?, ?);";
    sqlite3_stmt* stmt;

    int rc = sqlite3_prepare_v2(db, insertSQL, -1, &stmt, nullptr);
    if (rc != SQLITE_OK) {
        std::cerr << "Failed to prepare statement: " << sqlite3_errmsg(db) << std::endl;
        return;
    }

    sqlite3_bind_text(stmt, 1, username.c_str(), -1, SQLITE_STATIC);
    sqlite3_bind_text(stmt, 2, hashedPassword.c_str(), -1, SQLITE_STATIC);

    rc = sqlite3_step(stmt);
    if (rc != SQLITE_DONE) {
        std::cerr << "Error inserting data: " << sqlite3_errmsg(db) << std::endl;
    } else {
        std::cout << "User registered successfully!" << std::endl;
    }

    sqlite3_finalize(stmt);
}

int main() {
    // Open the SQLite database
    sqlite3* db = openDatabase("users.db");
    if (db == nullptr) {
        return -1;  // Exit if the database couldn't be opened
    }

    // Create the users table if it doesn't exist
    createUsersTable(db);

    std::string username, password;

    // Collect username and password from the user
    std::cout << "Enter username: ";
    std::getline(std::cin, username);
    std::cout << "Enter password: ";
    std::getline(std::cin, password);

    // Hash the password using MD5
    std::string hashedPassword = md5Hash(password);

    // Insert the user data into the database
    insertUser(db, username, hashedPassword);

    // Close the SQLite database
    sqlite3_close(db);

    return 0;
}
