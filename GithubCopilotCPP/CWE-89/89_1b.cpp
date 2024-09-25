#include <iostream>
#include <string>
#include <unordered_set>
#include "httplib.h"

// Mock database using an unordered_set
std::unordered_set<std::string> database = {"user1@example.com", "user2@example.com"};

int main() {
    httplib::Server svr;

    svr.Get("/unsubscribe", [](const httplib::Request& req, httplib::Response& res) {
        auto email = req.get_param_value("email");

        if (database.find(email) != database.end()) {
            // Email found in the database, proceed to unsubscribe
            database.erase(email);
            res.set_content("You have been unsubscribed successfully.", "text/plain");
        } else {
            // Email not found in the database
            res.set_content("The email is not subscribed.", "text/plain");
        }
    });

    std::cout << "Server is running on http://localhost:8080" << std::endl;
    svr.listen("localhost", 8080);

    return 0;
}