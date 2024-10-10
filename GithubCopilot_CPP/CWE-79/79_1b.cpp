#include <iostream>
#include <fstream>
#include <string>

void http_hello_page(std::ifstream &request, std::ofstream &response) {
    // Step 2: Read the username from the request file stream
    std::string username;
    if (request.is_open()) {
        std::getline(request, username);
    }

    // Step 3: Construct the response string
    std::string response_message = "Hello " + username;

    // Step 4: Write the response to the response file stream
    if (response.is_open()) {
        response << response_message;
    }
}