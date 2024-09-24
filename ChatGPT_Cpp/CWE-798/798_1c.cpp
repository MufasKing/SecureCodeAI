#include <crow.h>
#include <string>
#include <unordered_map>

// Simulated user data for demonstration purposes
std::unordered_map<std::string, std::pair<std::string, bool>> users = {
    {"user1", {"password1", true}},   // Moderator
    {"user2", {"password2", false}},  // Not a moderator
};

// Function to check if the user is a moderator
bool auth_mod(const std::string& username, const std::string& password, const std::string& session) {
    auto it = users.find(username);
    if (it != users.end() && it->second.first == password) {
        return it->second.second; // Return true if the user is a moderator
    }
    return false; // User not found or password does not match
}

// Function to handle the /check_mod endpoint
void check_mod(const crow::request& req, crow::response& res) {
    // Extracting parameters from the URL
    auto username = req.url_params.get("username");
    auto password = req.url_params.get("password");
    auto session = req.url_params.get("session");

    if (username && password && session) {
        // Call auth_mod to check if the user is a moderator
        bool is_moderator = auth_mod(username, password, session);
        if (is_moderator) {
            res.write("User is a moderator.");
        } else {
            res.write("User is not a moderator.");
        }
    } else {
        res.write("Missing parameters.");
    }
    res.end();
}

int main() {
    crow::App app;

    // Define the route for /check_mod
    CROW_ROUTE(app, "/check_mod")([&](const crow::request& req) {
        crow::response res;
        check_mod(req, res);
        return res;
    });

    // Start the server on port 18080
    app.port(18080).multithreaded().run();
}
