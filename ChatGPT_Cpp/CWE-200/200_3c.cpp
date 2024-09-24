#include <cpprest/http_listener.h>
#include <cpprest/uri.h>
#include <cpprest/json.h>
#include <cpprest/uri.h>
#include <map>
#include <string>
#include <iostream>

using namespace web;                     // Commonly used classes from C++ REST SDK
using namespace web::http;              // HTTP library
using namespace web::http::experimental::listener; // HTTP listener

// Simulated session storage
std::map<std::string, std::string> session; // Simple key-value session storage

// Function to retrieve user info from the session
void info(http_request request) {
    // Check for GET method
    if (request.method() == methods::GET) {
        json::value response_data;
        
        // Retrieve data from the session
        auto username = session.find("username") != session.end() ? session["username"] : "Unknown User";
        auto email = session.find("email") != session.end() ? session["email"] : "Unknown Email";
        auto ssn = session.find("ssn") != session.end() ? session["ssn"] : "Unknown SSN";

        // Populate the JSON response
        response_data[U("username")] = json::value::string(username);
        response_data[U("email")] = json::value::string(email);
        response_data[U("ssn")] = json::value::string(ssn);

        // Send response
        request.reply(status_codes::OK, response_data);
    } else {
        // Handle other methods
        request.reply(status_codes::MethodNotAllowed, U("Method not allowed"));
    }
}

int main() {
    // Create a listener for the specified URL
    uri_builder uri(U("http://localhost:8080/info"));
    auto addr = uri.to_uri().to_string();
    http_listener listener(addr);

    // Set session data for testing
    session["username"] = "JohnDoe";
    session["email"] = "john.doe@example.com";
    session["ssn"] = "123-45-6789";

    // Register the info function for the /info route
    listener.support(methods::GET, info);

    // Start listening for incoming requests
    listener
        .open()
        .then([&listener](){ std::wcout << U("Starting to listen at: ") << listener.uri().to_string() << std::endl; })
        .wait();

    // Keep the application running
    std::string line;
    std::getline(std::cin, line);
    return 0;
}
