#include "crow.h"
#include <string>

// Mock session data
struct Session {
    std::string username;
    std::string email;
    std::string ssn;
};

// Function to get user info from session
std::string info(const Session& session) {
    return "Username: " + session.username + "\nEmail: " + session.email + "\nSSN: " + session.ssn;
}

int main() {
    crow::SimpleApp app;

    // Mock session data
    Session session = {"john_doe", "john@example.com", "123-45-6789"};

    // Define the /info route
    CROW_ROUTE(app, "/info")
    ([&session]() {
        return info(session);
    });

    // Start the server
    app.port(18080).multithreaded().run();
}