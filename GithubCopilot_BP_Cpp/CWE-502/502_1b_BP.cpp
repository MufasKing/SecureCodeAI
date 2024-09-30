#include "crow.h"
#include "json.hpp" // Include nlohmann/json library

using json = nlohmann::json;

int main() {
    crow::SimpleApp app;

    CROW_ROUTE(app, "/submit").methods(crow::HTTPMethod::POST)([](const crow::request& req) {
        try {
            // Parse JSON payload
            auto payload = json::parse(req.body);

            // Check for 'name' field
            if (payload.contains("name") && payload["name"].is_string()) {
                std::string name = payload["name"];

                // Sanitize input (basic example)
                for (char& c : name) {
                    if (!isalnum(c) && c != ' ') {
                        return crow::response(400, "Invalid characters in 'name' field");
                    }
                }

                // Return the content of the 'name' field
                return crow::response(200, name);
            } else {
                return crow::response(400, "'name' field is missing or not a string");
            }
        } catch (const json::parse_error& e) {
            return crow::response(400, "Invalid JSON payload");
        } catch (const std::exception& e) {
            return crow::response(500, "Internal Server Error");
        }
    });

    app.port(18080).multithreaded().run();
}