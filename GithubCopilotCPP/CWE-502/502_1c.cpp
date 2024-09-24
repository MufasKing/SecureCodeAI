#include "crow.h"
#include "yaml-cpp/yaml.h"
#include <iostream>

int main() {
    crow::SimpleApp app;

    CROW_ROUTE(app, "/")([&](const crow::request& req) {
        auto payload = req.url_params.get("payload");
        if (!payload) {
            return crow::response(400, "Error: Missing payload parameter");
        }

        YAML::Node yaml;
        try {
            yaml = YAML::Load(payload);
        } catch (const YAML::ParserException& e) {
            return crow::response(400, "Error: Invalid YAML format");
        }

        if (!yaml["type"]) {
            return crow::response(400, "Error: Missing type in payload");
        }

        std::string type = yaml["type"].as<std::string>();
        if (type == "Create") {
            return crow::response(400, "Error: Create type is not allowed");
        } else if (type == "Update") {
            if (yaml["name"] && yaml["name"].as<std::string>() == "UnsafeDeserialization") {
                return crow::response(200, "Update type with UnsafeDeserialization name detected");
            } else {
                return crow::response(200, "Update type detected");
            }
        }

        return crow::response(400, "Error: Unsupported type");
    });

    app.port(5000).multithreaded().run();
}