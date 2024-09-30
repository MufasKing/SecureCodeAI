#include <iostream>
#include <string>
#include <pistache/endpoint.h>
#include <sqlite3.h>
#include <openssl/sha.h>
#include <nlohmann/json.hpp>

using json = nlohmann::json;
using namespace Pistache;

// Function to hash the password
std::string hashPassword(const std::string& password) {
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256(reinterpret_cast<const unsigned char*>(password.c_str()), password.length(), hash);
    
    std::string hashedPassword;
    for (int i = 0; i < SHA256_DIGEST_LENGTH; i++) {
        hashedPassword += sprintf("%02x", hash[i]);
    }
    return hashedPassword;
}

// Function to register user
void registerUser(const std::string& username, const std::string& password) {
    sqlite3* db;
    sqlite3_stmt* stmt;

    // Open database
    if (sqlite3_open("users.db", &db)) {
        std::cerr << "Can't open database: " << sqlite3_errmsg(db) << std::endl;
        return;
    }

    // Create table if it doesn't exist
    const char* createTableQuery = R"(
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        );
    )";
    sqlite3_exec(db, createTableQuery, nullptr, nullptr, nullptr);

    // Prepare the insert statement with placeholders
    const char* insertQuery = "INSERT INTO users (username, password) VALUES (?, ?);";
    if (sqlite3_prepare_v2(db, insertQuery, -1, &stmt, nullptr) != SQLITE_OK) {
        std::cerr << "Failed to prepare statement: " << sqlite3_errmsg(db) << std::endl;
        sqlite3_close(db);
        return;
    }

    // Bind parameters
    sqlite3_bind_text(stmt, 1, username.c_str(), -1, SQLITE_STATIC);
    sqlite3_bind_text(stmt, 2, hashPassword(password).c_str(), -1, SQLITE_STATIC);

    // Execute statement
    if (sqlite3_step(stmt) != SQLITE_DONE) {
        std::cerr << "Failed to execute statement: " << sqlite3_errmsg(db) << std::endl;
    } else {
        std::cout << "User registered successfully!" << std::endl;
    }

    // Clean up
    sqlite3_finalize(stmt);
    sqlite3_close(db);
}

// HTTP handler for registration
class RegistrationHandler : public Http::Handler {
public:
    HTTP_PROTOTYPE(RegistrationHandler)

    void onRequest(const Http::Request& request, Http::ResponseWriter response) override {
        // Input validation
        auto body = request.body();
        auto jsonData = json::parse(body);
        std::string username = jsonData["username"];
        std::string password = jsonData["password"];

        // Simple validation
        if (username.empty() || password.length() < 8) {
            response.send(Http::Code::Bad_Request, "Username must not be empty and password must be at least 8 characters long.");
            return;
        }

        registerUser(username, password);
        response.send(Http::Code::Ok, "Registration successful.");
    }
};

int main() {
    // Create and configure the HTTP server
    Http::listenAndServe<RegistrationHandler>("*:8080");
    return 0;
}
