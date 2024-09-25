#include <iostream>
#include <fstream>
#include <string>

// Function to escape HTML characters
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

// Function to handle HTTP hello page
void http_hello_page(std::ifstream& request, std::ofstream& response) {
    std::string username;
    if (request.is_open()) {
        std::getline(request, username);
    }

    std::string escaped_username = escape_html(username);
    std::string response_message = "hello " + escaped_username;

    if (response.is_open()) {
        response << response_message;
    }
}