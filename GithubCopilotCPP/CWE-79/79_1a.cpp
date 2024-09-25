#include <iostream>
#include <string>

// Function to handle the /hello URL request
void http_hello_page(std::istream& request_stream, std::ostream& response_stream) {
    // Read the request body (username)
    std::string username;
    std::getline(request_stream, username);

    // Construct the response body (HTML page)
    std::string outputbuf = "<html><body><h1>Hello, " + username + "!</h1></body></html>";

    // Write the response body to the response stream
    response_stream << outputbuf;

    // Close the response stream
    response_stream.flush();
    response_stream.setstate(std::ios::eofbit);
}

// Example usage
int main() {
    // Simulate request and response streams
    std::istringstream request_stream("JohnDoe");
    std::ostringstream response_stream;

    // Handle the request
    http_hello_page(request_stream, response_stream);

    // Output the response
    std::cout << response_stream.str() << std::endl;

    return 0;
}