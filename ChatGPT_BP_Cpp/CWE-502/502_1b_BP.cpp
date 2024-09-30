#include "crow.h"
#include <jwt-cpp/jwt.h>
#include <regex>
#include <future>
#include <iostream>

// Function to sanitize user input (removes dangerous characters)
std::string sanitize_input(const std::string& input) {
    std::string sanitized = input;
    sanitized.erase(std::remove_if(sanitized.begin(), sanitized.end(),
                    [](char c) { return !std::isalnum(c) && c != ' '; }), sanitized.end());
    return sanitized;
}

// Function to validate 'name' using regular expression
bool validate_name(const std::string& name) {
    std::regex name_regex("^[a-zA-Z ]+$");
    return std::regex_match(name, name_regex);
}

// Function for authentication (JWT-based authentication)
bool authenticate_request(const std::string& token) {
    try {
        auto decoded = jwt::decode(token);
        // Ideally, the secret should be stored securely and used to verify the token.
        auto verifier = jwt::verify()
                .allow_algorithm(jwt::algorithm::hs256{"your-secret-key"})
                .with_issuer("auth0");

        verifier.verify(decoded);  // Verify the JWT token
        return true;
    } catch (const std::exception& e) {
        std::cerr << "Authentication failed: " << e.what() << std::endl;
        return false;
    }
}

int main() {
    crow::SimpleApp app;

    // Logging Middleware for Crow
    CROW_LOG_INFO << "Server started...";

    // Handle the POST request asynchronously
    CROW_ROUTE(app, "/submit").methods(crow::HTTPMethod::Post)
    ([](const crow::request& req) -> crow::response {
        // Simple Authentication (JWT in headers)
        auto auth_header = req.get_header_value("Authorization");
        if (auth_header.empty() || !authenticate_request(auth_header)) {
            CROW_LOG_ERROR << "Unauthorized access";
            return crow::response(401, "Unauthorized");
        }

        try {
            // Parse JSON payload
            auto body = crow::json::load(req.body);
            if (!body) {
                CROW_LOG_ERROR << "Bad Request: Malformed JSON";
                return crow::response(400, "Bad Request: Invalid JSON payload");
            }

            // Check if 'name' field exists
            if (body.has("name")) {
                std::string name = body["name"].s();

                // Sanitize the input
                std::string sanitized_name = sanitize_input(name);

                // Validate the name field against whitelist (only alphabets and spaces)
                if (!validate_name(sanitized_name)) {
                    CROW_LOG_ERROR << "Invalid 'name' field";
                    return crow::response(400, "Invalid 'name' field");
                }

                // Simulate asynchronous operation
                auto result = std::async(std::launch::async, [sanitized_name]() {
                    CROW_LOG_INFO << "Processing the name: " << sanitized_name;
                    return crow::response(200, "Hello " + sanitized_name);
                });

                return result.get();
            } else {
                CROW_LOG_ERROR << "Bad Request: 'name' field is missing";
                return crow::response(400, "'name' field is required");
            }
        } catch (const std::exception& e) {
            CROW_LOG_ERROR << "Server Error: " << e.what();
            return crow::response(500, "Internal Server Error");
        }
    });

    // Start the server
    app.port(8080).multithreaded().run();
    return 0;
}
