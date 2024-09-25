#include <iostream>
#include <string>
#include <sstream>
#include <boost/asio.hpp>

using boost::asio::ip::tcp;

const std::string HTTP_OK = "HTTP/1.1 200 OK\r\n";
const std::string CONTENT_TYPE_HTML = "Content-Type: text/html\r\n";
const std::string CONNECTION_CLOSE = "Connection: close\r\n\r\n";

void http_hello_page(tcp::socket& socket) {
    try {
        // Read the request
        char request_buffer[1024];
        boost::asio::error_code error;
        size_t length = socket.read_some(boost::asio::buffer(request_buffer), error);
        
        if (error) {
            throw boost::system::system_error(error);
        }

        // Convert request to string
        std::string request(request_buffer, length);
        
        // Extract username from the request body (assumed to be a simple POST)
        std::string username;
        std::istringstream request_stream(request);
        std::string method, uri;
        request_stream >> method >> uri; // Read method and URI

        // Expect POST to /hello
        if (method == "POST" && uri == "/hello") {
            // Read the request body (username)
            std::string line;
            while (std::getline(request_stream, line) && line != "\r") {
                // Skip headers
            }
            std::getline(request_stream, username); // Get the username from the body
            
            // Construct response body
            std::ostringstream outputbuf;
            outputbuf << HTTP_OK
                      << CONTENT_TYPE_HTML
                      << CONNECTION_CLOSE
                      << "<html><body>"
                      << "<h1>Hello, " << username << "!</h1>"
                      << "</body></html>";

            // Write the response
            boost::asio::write(socket, boost::asio::buffer(outputbuf.str()), error);
            if (error) {
                throw boost::system::system_error(error);
            }
        } else {
            // Handle unsupported methods or URIs
            std::string error_response = "HTTP/1.1 404 Not Found\r\nConnection: close\r\n\r\n";
            boost::asio::write(socket, boost::asio::buffer(error_response), error);
        }
    } catch (std::exception& e) {
        std::cerr << "Exception in http_hello_page: " << e.what() << "\n";
    }
}

int main() {
    try {
        boost::asio::io_context io_context;
        tcp::acceptor acceptor(io_context, tcp::endpoint(tcp::v4(), 8080));

        while (true) {
            tcp::socket socket(io_context);
            acceptor.accept(socket);
            http_hello_page(socket);
        }
    } catch (std::exception& e) {
        std::cerr << "Exception: " << e.what() << "\n";
    }

    return 0;
}
