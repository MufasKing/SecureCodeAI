#include "crow_all.h"
#include <nlohmann/json.hpp> // For JSON handling
#include <iostream>

using json = nlohmann::json;

int main() {
    crow::SimpleApp app;

    // Define the /api route
    CROW_ROUTE(app, "/api")([&](const crow::request& req) {
        // Get the 'payload' parameter from the URL
        auto payload_param = req.url_params.get("payload");
        if (!payload_param) {
            return crow::response(400, "Missing 'payload' parameter");
        }

        // Parse the payload into a JSON object
        json payload_json;
        try {
            payload_json = json::parse(payload_param);
        } catch (const json::parse_error& e) {
            return crow::response(400, "Invalid JSON payload");
        }

        // Check if 'name' exists in the payload
        if (payload_json.contains("name")) {
            std::string name_value = payload_json["name"];
            return crow::response(200, name_value); // Return the name value
        } else {
            return crow::response(400, "'name' key not found in payload");
        }
    });

    app.port(8080).multithreaded().run(); // Start the app on port 8080
}
