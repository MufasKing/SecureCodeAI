#include <iostream>
#include <string>
#include <unordered_map>
#include <crow.h>
#include <json/json.h>

int main() {
    crow::SimpleApp app;

    CROW_ROUTE(app, "/api")
    ([](const crow::request& req) {
        auto query_params = crow::query_string(req.url_params);
        std::string payload = query_params.get("payload");

        Json::Value root;
        Json::CharReaderBuilder reader;
        std::string errs;

        std::istringstream s(payload);
        if (!Json::parseFromStream(reader, s, &root, &errs)) {
            return crow::response(400, "Invalid JSON payload");
        }

        if (!root.isMember("name")) {
            return crow::response(400, "Missing 'name' in payload");
        }

        std::string name = root["name"].asString();
        return crow::response(200, name);
    });

    app.port(8080).multithreaded().run();
}