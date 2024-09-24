#include <iostream>
#include <cpprest/http_listener.h>
#include <cpprest/json.h>

using namespace web;             // Common features like URIs and JSON
using namespace web::http;      // Common HTTP functionality
using namespace web::http::experimental::listener; // HTTP listener

// Function to return a database connection (simulated)
std::string getDatabaseConnection() {
    return "Database connection established.";
}

// Function to return the server name
std::string getServerName() {
    return "localhost";
}

// Function to return the database name
std::string getDatabaseName() {
    return "my_database";
}

// Function to return the database user
std::string getDatabaseUser() {
    return "db_user";
}

// Function to return the database password
std::string getDatabasePassword() {
    return "db_password";
}

// Function to handle HTTP GET requests
void handle_get(http_request request) {
    json::value response_data;

    // Populate the response data with database information
    response_data[U("connection")] = json::value::string(getDatabaseConnection());
    response_data[U("server_name")] = json::value::string(getServerName());
    response_data[U("database_name")] = json::value::string(getDatabaseName());
    response_data[U("database_user")] = json::value::string(getDatabaseUser());
    response_data[U("database_password")] = json::value::string(getDatabasePassword());

    // Send the response
    request.reply(status_codes::OK, response_data);
}

int main() {
    uri uri(U("http://localhost:8080"));
    http_listener listener(uri);

    listener.support(methods::GET, handle_get);

    try {
        listener
            .open()
            .then([&listener](){ std::wcout << L"Starting to listen at: " << listener.uri().to_string() << std::endl; })
            .wait();

        std::string line;
        std::getline(std::cin, line); // Keep the app running
    } catch (const std::exception& e) {
        std::cerr << "An error occurred: " << e.what() << std::endl;
    }

    return 0;
}
