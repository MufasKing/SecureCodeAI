#include "crow.h"
#include <openssl/sha.h>
#include <openssl/rand.h>
#include <unordered_map>
#include <regex>
#include <string>
#include <iostream>

// A simple in-memory session storage (for demo purposes)
std::unordered_map<std::string, crow::json::wvalue> session_store;

// Dummy database for users (in real-world, use proper database storage)
struct User {
    std::string username;
    std::string email;
    std::string hashed_password;
    std::string ssn;
};

std::unordered_map<std::string, User> user_db = {
    {"john_doe", {"john_doe", "john@example.com", "5e88489f", "123456789"}}
};

// Function to hash passwords using SHA-256
std::string hash_password(const std::string& password) {
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256_CTX sha256;
    SHA256_Init(&sha256);
    SHA256_Update(&sha256, password.c_str(), password.size());
    SHA256_Final(hash, &sha256);

    char buffer[65];
    for (int i = 0; i < SHA256_DIGEST_LENGTH; i++) {
        sprintf(buffer + (i * 2), "%02x", hash[i]);
    }
    buffer[64] = 0;
    return std::string(buffer);
}

// Input validation function
bool validate_input(const std::string& username, const std::string& password) {
    // Validate using regex (e.g., alphanumeric for username, strong password)
    std::regex username_pattern("^[a-zA-Z0-9_]{3,16}$");
    std::regex password_pattern("^(?=.*[A-Za-z])(?=.*\\d)[A-Za-z\\d]{8,}$");

    return std::regex_match(username, username_pattern) &&
           std::regex_match(password, password_pattern);
}

// Sanitize input to prevent XSS attacks
std::string sanitize_input(const std::string& input) {
    std::string sanitized = input;
    std::replace(sanitized.begin(), sanitized.end(), '<', '[');
    std::replace(sanitized.begin(), sanitized.end(), '>', ']');
    return sanitized;
}

// Function to authenticate user
bool authenticate(const std::string& username, const std::string& password) {
    auto it = user_db.find(username);
    if (it != user_db.end()) {
        std::string hashed_password = hash_password(password);
        return it->second.hashed_password == hashed_password;
    }
    return false;
}

// Middleware to check if the user is authenticated
bool is_authenticated(const std::string& session_id) {
    return session_store.find(session_id) != session_store.end();
}

// Error page handler
crow::response error_page(const std::string& message) {
    crow::json::wvalue error_response;
    error_response["error"] = message;
    return crow::response(400, error_response);
}

int main() {
    crow::SimpleApp app;

    // Secure transmission (HTTPS should be configured properly in production)
    CROW_ROUTE(app, "/login")
        .methods("POST"_method)
    ([&](const crow::request& req) {
        auto body = crow::json::load(req.body);
        if (!body) {
            return error_page("Invalid input");
        }

        std::string username = sanitize_input(body["username"].s());
        std::string password = sanitize_input(body["password"].s());

        // Validate input
        if (!validate_input(username, password)) {
            return error_page("Invalid username or password format.");
        }

        // Authenticate user
        if (!authenticate(username, password)) {
            return error_page("Authentication failed.");
        }

        // Create a new session (for demo, session id is just random)
        std::string session_id = crow::utility::random_string(32);

        session_store[session_id] = {{"username", username}, {"email", user_db[username].email}, {"ssn", user_db[username].ssn}};

        // Return the session ID as a cookie
        crow::response res;
        res.set_header("Set-Cookie", "session_id=" + session_id + "; HttpOnly; Secure; SameSite=Strict;");
        res.code = 200;
        res.body = "Login successful";
        return res;
    });

    // Secure route to access user info
    CROW_ROUTE(app, "/info").methods("GET"_method)([](const crow::request& req) {
        std::string session_id = req.get_header_value("Cookie");

        // Check if the session is valid
        if (session_id.empty() || !is_authenticated(session_id)) {
            return error_page("Unauthorized access. Please log in.");
        }

        auto session_data = session_store[session_id];
        std::string username = session_data["username"].s();
        std::string email = session_data["email"].s();
        std::string ssn = session_data["ssn"].s();

        // Mask SSN (only showing last 4 digits)
        std::string masked_ssn = "XXX-XX-" + ssn.substr(ssn.length() - 4);

        crow::json::wvalue result;
        result["username"] = sanitize_input(username);
        result["email"] = sanitize_input(email);
        result["ssn"] = masked_ssn;

        return crow::response(200, result);
    });

    // Secure server settings (SSL/TLS)
    // NOTE: In production, configure actual SSL certificates
    app.bindaddr("0.0.0.0").port(18080).run();
}
