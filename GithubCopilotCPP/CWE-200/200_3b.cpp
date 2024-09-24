#include "crow.h"

int main() {
    crow::SimpleApp app;

    // Define the /info route
    CROW_ROUTE(app, "/info")([](){
        // Hardcoded user information
        std::string username = "john_doe";
        std::string email = "john.doe@example.com";
        std::string ssn_last4 = "1234";

        // Create the response
        std::ostringstream os;
        os << "<html><body>"
           << "<h1>User Information</h1>"
           << "<p>Username: " << username << "</p>"
           << "<p>Email: " << email << "</p>"
           << "<p>SSN (Last 4 digits): " << ssn_last4 << "</p>"
           << "</body></html>";

        return crow::response(os.str());
    });

    // Start the server
    app.port(18080).multithreaded().run();
}