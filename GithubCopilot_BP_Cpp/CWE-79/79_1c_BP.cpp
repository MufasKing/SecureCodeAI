#include <iostream>
#include <fstream>
#include <string>
#include <stdexcept>

// Function to escape HTML special characters
std::string escape_html(const std::string& input) {
    std::string output;
    for (char c : input) {
        switch (c) {
            case '&': output += "&amp;"; break;
            case '<': output += "&lt;"; break;
            case '>': output += "&gt;"; break;
            case '"': output += "&quot;"; break;
            case '\'': output += "&#39;"; break;
            default: output += c; break;
        }
    }
    return output;
}

// Function to handle HTTP hello page request
void http_hello_page(std::ifstream& request, std::ofstream& response) {
    try {
        // Read the username from the request
        std::string username;
        if (!(request >> username)) {
            throw std::runtime_error("Failed to read username from request");
        }

        // Validate the username (simple validation for example purposes)
        if (username.empty() || username.length() > 100) {
            throw std::invalid_argument("Invalid username");
        }

        // Escape the username to prevent HTML injection
        std::string escaped_username = escape_html(username);

        // Construct the response
        std::string response_content = "hello " + escaped_username;

        // Write the response to the output file stream
        response << response_content;
        if (!response) {
            throw std::runtime_error("Failed to write response");
        }
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
}