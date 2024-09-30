#include <crow.h>
#include <mysql++/mysql++.h>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <regex>
#include <jwt-cpp/jwt.h>  // Use JWT for token-based authentication

// Secure password hashing library (e.g., bcrypt or argon2 can be used)
#include <bcrypt/BCrypt.hpp>

// Function to check if user is a moderator
bool is_moderator(const std::string& username, mysqlpp::Connection& db_conn) {
    try {
        // Prepared statement to prevent SQL Injection
        mysqlpp::Query query = db_conn.query();
        query << "SELECT is_moderator FROM users WHERE username = %0q:username";

        query.parse();
        mysqlpp::StoreQueryResult res = query.store(username);

        if (res.empty()) {
            return false;  // User not found
        }

        return res[0]["is_moderator"] == "1";
    } catch (const mysqlpp::BadQuery& e) {
        std::cerr << "Query error: " << e.what() << std::endl;
        throw std::runtime_error("Database query error.");
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        throw std::runtime_error("Internal server error.");
    }
}

// Middleware for basic token-based authentication
std::string authenticate(const crow::request& req) {
    const auto auth_header = req.get_header_value("Authorization");
    if (auth_header.empty()) {
        throw std::runtime_error("No authorization header found.");
    }

    std::string token = auth_header.substr(7);  // Bearer token
    try {
        // Parse JWT token
        auto decoded_token = jwt::decode(token);
        auto verifier = jwt::verify()
            .allow_algorithm(jwt::algorithm::hs256{"secret"})
            .with_issuer("auth0");
        verifier.verify(decoded_token);

        return decoded_token.get_payload_claim("username").as_string();
    } catch (const std::exception& e) {
        throw std::runtime_error("Invalid token.");
    }
}

int main() {
    crow::SimpleApp app;

    // Secure Database connection
    mysqlpp::Connection db_conn(false);

    try {
        // Use SSL connection to the database for encryption
        mysqlpp::SSLOptions ssl_opt;
        ssl_opt.key_file = "/path/to/client-key.pem";
        ssl_opt.cert_file = "/path/to/client-cert.pem";
        ssl_opt.ca_file = "/path/to/ca-cert.pem";

        db_conn.set_option(&ssl_opt);
        db_conn.connect("dbname", "dbhost", "username", "password");

        std::cout << "Connected to database." << std::endl;
    } catch (const mysqlpp::ConnectionFailed& e) {
        std::cerr << "Database connection error: " << e.what() << std::endl;
        return 1;
    }

    // Route to check if user is a moderator
    CROW_ROUTE(app, "/check_moderator")
        .methods("POST"_method)([&db_conn](const crow::request& req) {
            try {
                // Authenticate the user using token-based authentication
                std::string username = authenticate(req);

                // Input Validation: Check if username is valid
                if (!std::regex_match(username, std::regex("^[a-zA-Z0-9_]{3,30}$"))) {
                    throw std::invalid_argument("Invalid username format.");
                }

                // Check if user is a moderator
                bool moderator_status = is_moderator(username, db_conn);

                // Return the result
                crow::json::wvalue result;
                result["username"] = username;
                result["is_moderator"] = moderator_status;
                return crow::response(200, result);
            } catch (const std::invalid_argument& e) {
                crow::json::wvalue error;
                error["error"] = e.what();
                return crow::response(400, error);
            } catch (const std::exception& e) {
                crow::json::wvalue error;
                error["error"] = "Authentication failed.";
                return crow::response(401, error);
            }
        });

    // Error handling middleware
    app.loglevel(crow::LogLevel::Warning); // Set log level
    app.port(8080).multithreaded().run();

    return 0;
}
