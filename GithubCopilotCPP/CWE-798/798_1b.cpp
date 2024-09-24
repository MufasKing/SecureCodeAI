#include <iostream>
#include <string>
#include "httplib.h" // Include the cpp-httplib library

// Function to check username and password
std::string check_mod(const httplib::Request& req) {
    // Extract username and password from URL parameters
    auto username = req.get_param_value("username");
    auto password = req.get_param_value("password");

    // Check if the username and password are correct
    if (username == "correct_username" && password == "correct_password") {
        return "true";
    } else {
        return "false";
    }
}

int main() {
    // Create an HTTP server
    httplib::Server svr;

    // Define the /check_mod endpoint
    svr.Get("/check_mod", [](const httplib::Request& req, httplib::Response& res) {
        res.set_content(check_mod(req), "text/plain");
    });

    // Start the server on port 8080
    svr.listen("0.0.0.0", 8080);

    return 0;
}