#include "crow.h"
#include <regex>

int main() {
    crow::SimpleApp app;

    // Define the route
    CROW_ROUTE(app, "/redirect")
    ([&](const crow::request& req) {
        auto target = req.url_params.get("target");
        if (!target) {
            return crow::response(400, "Bad Request: target parameter is missing");
        }

        // Define the regular expression
        std::regex url_regex(".*example\\.com.*");

        // Check if the target matches the regular expression
        if (std::regex_match(target, url_regex)) {
            return crow::response(302, target); // Redirect to the target
        } else {
            return crow::response(302, "/"); // Redirect to "/"
        }
    });

    // Run the server
    app.port(18080).multithreaded().run();
}