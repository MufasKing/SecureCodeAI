#include <iostream>
#include <string>
#include <regex>
#include "httplib.h"
#include "sqlite3.h"
#include "bcrypt/BCrypt.hpp"

// Function to validate input
bool validate_input(const std::string& input) {
    std::regex pattern("^[a-zA-Z0-9_]{3,20}$");
    return std::regex_match(input, pattern);
}

// Function to connect to the database
sqlite3* connect_db() {
    sqlite3* db;
    if (sqlite3_open("users.db", &db)) {
        std::cerr << "Can't open database: " << sqlite3_errmsg(db) << std::endl;
        return nullptr;
    }
    return db;
}

// Function to create users table
void create_table(sqlite3* db) {
    const char* sql = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT);";
    char* errMsg = nullptr;
    if (sqlite3_exec(db, sql, nullptr, nullptr, &errMsg) != SQLITE_OK) {
        std::cerr << "SQL error: " << errMsg << std::endl;
        sqlite3_free(errMsg);
    }
}

// Function to register a user
bool register_user(sqlite3* db, const std::string& username, const std::string& password) {
    std::string hashed_password = BCrypt::generateHash(password);
    sqlite3_stmt* stmt;
    const char* sql = "INSERT INTO users (username, password) VALUES (?, ?);";
    if (sqlite3_prepare_v2(db, sql, -1, &stmt, nullptr) != SQLITE_OK) {
        std::cerr << "Failed to prepare statement: " << sqlite3_errmsg(db) << std::endl;
        return false;
    }
    sqlite3_bind_text(stmt, 1, username.c_str(), -1, SQLITE_STATIC);
    sqlite3_bind_text(stmt, 2, hashed_password.c_str(), -1, SQLITE_STATIC);
    if (sqlite3_step(stmt) != SQLITE_DONE) {
        std::cerr << "Failed to execute statement: " << sqlite3_errmsg(db) << std::endl;
        sqlite3_finalize(stmt);
        return false;
    }
    sqlite3_finalize(stmt);
    return true;
}

int main() {
    httplib::Server svr;

    // Initialize database
    sqlite3* db = connect_db();
    if (!db) return -1;
    create_table(db);

    // Register endpoint
    svr.Post("/register", [&](const httplib::Request& req, httplib::Response& res) {
        auto username = req.get_param_value("username");
        auto password = req.get_param_value("password");

        if (!validate_input(username) || !validate_input(password)) {
            res.set_content("Invalid input", "text/plain");
            return;
        }

        if (register_user(db, username, password)) {
            res.set_content("User registered successfully", "text/plain");
        } else {
            res.set_content("Failed to register user", "text/plain");
        }
    });

    svr.listen("localhost", 8080);

    sqlite3_close(db);
    return 0;
}