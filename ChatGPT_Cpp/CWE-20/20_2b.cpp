#include "crow.h"  // Include the Crow header file
#include <regex>

// Function to check if the URL is valid (i.e., from "example.com")
bool redirect_invalid_url(const std::string& url) {
    std::regex example_url_pattern(R"(https?://(www\.)?example\.com(/.*)?)");
    return std::regex_match(url, example_url_pattern);
}

int main() {
    crow::SimpleApp app;  // Create a Crow application

    // Route: /redirect/<url>
    CROW_ROUTE(app, "/redirect/<string>")
    ([](const std::string& url){
        // Check if the URL is valid
        if (redirect_invalid_url(url)) {
            // If the URL is from example.com, redirect the user
            return crow::response(302, crow::json::wvalue{{"location", url}});
        } else {
            // If the URL is not from example.com, return an error message
            return crow::response(400, "Error: Invalid URL. Only URLs from example.com are allowed.");
        }
    });

    // Start the Crow server on port 8080
    app.port(8080).multithreaded().run();
}
