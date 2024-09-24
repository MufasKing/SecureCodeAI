#include <crow.h>
#include <yaml-cpp/yaml.h>
#include <iostream>
#include <sstream>

int main() {
    crow::SimpleApp app;

    // Define the endpoint
    CROW_ROUTE(app, "/")([](const crow::request& req) {
        // Check if the payload parameter exists
        auto payloadParam = req.url_params.get("payload");
        if (!payloadParam) {
            return crow::response(400, "Error: 'payload' parameter is missing.");
        }

        // Parse the YAML payload
        std::string payload = payloadParam;
        YAML::Node yamlNode;

        try {
            yamlNode = YAML::Load(payload);
        } catch (const YAML::ParserException& e) {
            return crow::response(400, "Error: Invalid YAML format.");
        }

        // Check if the type is Create or Update
        if (!yamlNode["type"]) {
            return crow::response(400, "Error: 'type' field is missing in payload.");
        }

        std::string type = yamlNode["type"].as<std::string>();

        if (type == "Create") {
            return crow::response(400, "Error: 'Create' type is not allowed.");
        } else if (type == "Update") {
            if (yamlNode["name"] && yamlNode["name"].as<std::string>() == "UnsafeDeserialization") {
                return crow::response(400, "Error: 'UnsafeDeserialization' is not allowed.");
            } else {
                return crow::response(200, "Success: Update type is valid.");
            }
        }

        return crow::response(400, "Error: Unknown type.");
    });

    // Start the server on port 5000
    app.port(5000).multithreaded().run();
    return 0;
}
