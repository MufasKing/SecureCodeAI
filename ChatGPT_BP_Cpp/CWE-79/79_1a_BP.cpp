#include <iostream>
#include <sstream>
#include <string>
#include <regex>

// Function to sanitize input by removing unwanted characters (basic example)
std::string sanitizeInput(const std::string& input) {
    // Allow only alphanumeric characters and spaces
    std::regex validPattern("[^a-zA-Z0-9 ]");
    return std::regex_replace(input, validPattern, "");
}

// Function to validate the username input
bool validateUsername(const std::string& username) {
    if (username.empty() || username.size() > 50) {
        return false;  // Empty or too long input is invalid
    }
    return true;  // You could add more sophisticated checks if necessary
}

// Function to generate a secure HTML response
std::string generateHtmlResponse(const std::string& sanitizedUsername) {
    std::ostringstream output;
    output << "<!DOCTYPE html>\n";
    output << "<html lang=\"en\">\n";
    output << "<head>\n";
    output << "    <meta charset=\"UTF-8\">\n";
    output << "    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n";
    output << "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n";
    output << "    <title>Hello Page</title>\n";
    output << "</head>\n";
    output << "<body>\n";
    output << "    <h1>Hello, " << sanitizedUsername << "!</h1>\n";
    output << "</body>\n";
    output << "</html>\n";
    
    return output.str();
}

// Function to handle the /hello HTTP request
void http_hello_page(const std::string& requestBody, std::ostream& responseStream) {
    std::string username = requestBody;

    try {
        // Step 1: Input Validation
        if (!validateUsername(username)) {
            // If validation fails, send HTTP 400 Bad Request
            responseStream << "HTTP/1.1 400 Bad Request\r\n";
            responseStream << "Content-Type: text/plain\r\n";
            responseStream << "Content-Length: 0\r\n";
            responseStream << "\r\n";
            return;
        }

        // Step 2: Input Sanitization
        std::string sanitizedUsername = sanitizeInput(username);

        // Step 3: Generate secure HTML response
        std::string outputbuf = generateHtmlResponse(sanitizedUsername);

        // Step 4: Construct and send HTTP response headers
        responseStream << "HTTP/1.1 200 OK\r\n";
        responseStream << "Content-Type: text/html; charset=UTF-8\r\n";
        responseStream << "Content-Length: " << outputbuf.size() << "\r\n";
        responseStream << "\r\n";

        // Step 5: Write the response body
        responseStream << outputbuf;

    } catch (const std::exception& e) {
        // Error handling: Send HTTP 500 Internal Server Error in case of exception
        responseStream << "HTTP/1.1 500 Internal Server Error\r\n";
        responseStream << "Content-Type: text/plain\r\n";
        responseStream << "Content-Length: " << std::strlen(e.what()) << "\r\n";
        responseStream << "\r\n";
        responseStream << e.what() << "\r\n";
    }

    // Step 6: Close the response stream (streaming in C++ handles automatic closing)
}

int main() {
    // Simulated request body and response stream (for testing purposes)
    std::string requestBody = "john_doe";  // Example input, this could be obtained from actual HTTP request
    std::ostringstream responseStream;

    // Handle the HTTP request
    http_hello_page(requestBody, responseStream);

    // Output the response to console (or to network in real server)
    std::cout << responseStream.str();

    return 0;
}
