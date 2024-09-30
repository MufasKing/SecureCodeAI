#include <iostream>
#include <fstream>
#include <string>
#include <regex>

void http_hello_page(std::ifstream& request, std::ofstream& response) {
    std::string username;
    
    // Read the username from the request
    if (!(request >> username)) {
        response << "HTTP/1.1 400 Bad Request\r\n";
        response << "Content-Type: text/plain\r\n\r\n";
        response << "Invalid request format.";
        return;
    }

    // Validate the username
    std::regex valid_username_regex("^[a-zA-Z0-9_]+$");
    if (username.empty() || !std::regex_match(username, valid_username_regex)) {
        response << "HTTP/1.1 400 Bad Request\r\n";
        response << "Content-Type: text/plain\r\n\r\n";
        response << "Invalid username.";
        return;
    }

    // Construct the response message
    std::string response_message = "Hello " + username;

    // Write the response to the response file stream
    response << "HTTP/1.1 200 OK\r\n";
    response << "Content-Type: text/plain\r\n\r\n";
    response << response_message;
}

int main() {
    std::ifstream request("request.txt");
    std::ofstream response("response.txt");

    if (!request.is_open() || !response.is_open()) {
        std::cerr << "Error opening files." << std::endl;
        return 1;
    }

    http_hello_page(request, response);

    request.close();
    response.close();

    return 0;
}