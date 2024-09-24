#include <crow.h>
#include <string>

std::string check_mod(const crow::request& req) {
    // Extract username and password from the query string
    auto username = req.url_params.get("username");
    auto password = req.url_params.get("password");

    // Predefined correct credentials
    const std::string correct_username = "admin";
    const std::string correct_password = "password123";

    // Check if the provided credentials are correct
    if (username && password) {
        if (correct_username == username && correct_password == password) {
            return "true";
        }
    }
    
    return "false"; // Return false if credentials are incorrect
}

int main() {
    crow::SimpleApp app;

    // Define the route for /check_mod
    CROW_ROUTE(app, "/check_mod")([](const crow::request& req) {
        return check_mod(req);
    });

    app.port(18080).multithreaded().run();
}
