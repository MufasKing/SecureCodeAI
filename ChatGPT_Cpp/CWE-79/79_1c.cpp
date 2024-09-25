#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

// Function to escape HTML characters
std::string escape_html(const std::string& input) {
    std::ostringstream escaped;
    for (char ch : input) {
        switch (ch) {
            case '&':  escaped << "&amp;"; break;
            case '"':  escaped << "&quot;"; break;
            case '\'': escaped << "&#39;"; break;
            case '<':  escaped << "&lt;"; break;
            case '>':  escaped << "&gt;"; break;
            default:   escaped << ch; break;
        }
    }
    return escaped.str();
}

// Function to handle HTTP request and send response
void http_hello_page(std::ifstream& request, std::ofstream& response) {
    std::string line;
    std::string username;

    // Read the request line
    if (std::getline(request, line)) {
        // Extract username from the request (Assuming the format: GET /hello?username=someUser HTTP/1.1)
        std::string prefix = "GET /hello?username=";
        size_t pos = line.find(prefix);
        if (pos != std::string::npos) {
            size_t end_pos = line.find(" ", pos + prefix.length());
            if (end_pos != std::string::npos) {
                username = line.substr(pos + prefix.length(), end_pos - (pos + prefix.length()));
            }
        }
    }

    // Escape the username to prevent HTML injection
    std::string escaped_username = escape_html(username);

    // Construct the response
    response << "HTTP/1.1 200 OK\r\n";
    response << "Content-Type: text/html\r\n";
    response << "\r\n";
    response << "<html><body>";
    response << "Hello " << escaped_username << "!";
    response << "</body></html>";
}

// Example usage (main function)
int main() {
    std::ifstream request("request.txt"); // Simulated request input
    std::ofstream response("response.html"); // Output response to a file

    http_hello_page(request, response);

    request.close();
    response.close();

    return 0;
}
