#include <crow.h>

int main() {
    crow::SimpleApp app;

    // Route for /info
    CROW_ROUTE(app, "/info")([] {
        // Example user data (in a real application, this would come from a database or authentication system)
        std::string username = "john_doe";
        std::string email = "john.doe@example.com";
        std::string ssn_last4 = "1234"; // Last 4 digits of SSN

        // HTML response
        std::ostringstream response;
        response << "<html><body>"
                 << "<h1>User Information</h1>"
                 << "<p><strong>Username:</strong> " << username << "</p>"
                 << "<p><strong>Email:</strong> " << email << "</p>"
                 << "<p><strong>Last 4 Digits of SSN:</strong> " << ssn_last4 << "</p>"
                 << "</body></html>";
        
        return response.str();
    });

    app.port(8080).multithreaded().run(); // Start the server on port 8080
}
