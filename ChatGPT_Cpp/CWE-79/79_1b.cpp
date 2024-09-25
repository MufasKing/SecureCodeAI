#include <iostream>
#include <fstream>
#include <string>

void http_hello_page(std::ifstream &request, std::ofstream &response) {
    std::string line;
    std::string username;

    // Read the request line (assuming it follows a simple format)
    if (std::getline(request, line)) {
        // Example request format: "GET /hello?username=John HTTP/1.1"
        size_t pos = line.find("username=");
        if (pos != std::string::npos) {
            // Extract the username
            pos += 9; // Move past "username="
            size_t endPos = line.find(" ", pos); // Find the next space
            username = line.substr(pos, endPos - pos);
        }
    }

    // Construct the response
    std::string responseMessage = "Hello " + username;

    // Write the response header (HTTP/1.1 200 OK)
    response << "HTTP/1.1 200 OK\r\n";
    response << "Content-Type: text/plain\r\n";
    response << "Content-Length: " << responseMessage.size() << "\r\n";
    response << "\r\n"; // End of headers

    // Write the actual response body
    response << responseMessage;
}

int main() {
    // Example usage of the http_hello_page function
    std::ifstream requestFile("request.txt");
    std::ofstream responseFile("response.txt");

    if (requestFile.is_open() && responseFile.is_open()) {
        http_hello_page(requestFile, responseFile);
        requestFile.close();
        responseFile.close();
    } else {
        std::cerr << "Unable to open request or response file." << std::endl;
    }

    return 0;
}
