#include "crow.h"
#include <regex>
#include <string>

bool is_valid_url(const std::string& url) {
    // Regular expression to match URLs from example.com
    std::regex url_regex(R"(https?:\/\/(www\.)?example\.com\/?.*)");
    return std::regex_match(url, url_regex);
}

crow::response redirect_invalid_url(const std::string& url) {
    if (is_valid_url(url)) {
        // If the URL is valid (from example.com), redirect to the URL
        crow::response res;
        res.code = 302;  // HTTP 302 Found (redirect)
        res.add_header("Location", url);
        return res;
    } else {
        // If the URL is invalid, return an error message
        return crow::response(400, "Invalid URL. Only example.com URLs are allowed.");
    }
}

int main() {
    crow::SimpleApp app;

    // Define the route that takes a URL as a parameter
    CROW_ROUTE(app, "/redirect_url").methods(crow::HTTPMethod::GET)([](const crow::request& req) {
        auto url = req.url_params.get("url");
        if (!url) {
            return crow::response(400, "URL parameter is missing.");
        }

        // Call the function to check the URL and handle redirection or error
        return redirect_invalid_url(url);
    });

    // Start the application on port 8080
    app.port(8080).multithreaded().run();
}
