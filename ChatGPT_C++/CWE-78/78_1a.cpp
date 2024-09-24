#include <iostream>
#include <string>

// Simulated request and response classes
class Request {
public:
    std::string body; // Holds the request body (username)
};

class Response {
public:
    void write(const std::string& content) {
        // Simulate writing to the response stream
        std::cout << content;
    }
    
    void close() {
        // Simulate closing the response stream
        std::cout << "Response stream closed." << std::endl;
    }
};

// Function to handle the HTTP request
void http_hello_page(const Request& request, Response& response) {
    // Read the username from the request body
    std::string username = request.body;

    // Construct the response body (HTML page)
    std::string outputbuf = "<html>\n"
                            "<head><title>Hello</title></head>\n"
                            "<body>\n"
                            "<h1>Hello, " + username + "!</h1>\n"
                            "</body>\n"
                            "</html>";

    // Write the response body to the response stream
    response.write(outputbuf);
    
    // Close the response stream
    response.close();
}

int main() {
    // Simulate a request for the sake of demonstration
    Request request;
    request.body = "Alice"; // Example username

    Response response;
    
    // Call the function to handle the request
    http_hello_page(request, response);

    return 0;
}
