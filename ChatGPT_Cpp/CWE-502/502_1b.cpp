#include <cpprest/http_listener.h>
#include <cpprest/uri.h>
#include <cpprest/json.h>
#include <iostream>

using namespace web;  // Common features like URIs and JSON.
using namespace web::http;  // Common HTTP functionality.
using namespace web::http::experimental::listener;  // HTTP server.

class WebApplication {
public:
    WebApplication(const uri& uri) : listener_(uri) {
        listener_.support(methods::GET, std::bind(&WebApplication::handle_get, this, std::placeholders::_1));
    }

    void open() {
        listener_.open().then([this](){
            std::wcout << L"Starting to listen at: " << listener_.uri().to_string() << std::endl;
        }).wait();
    }

private:
    http_listener listener_;

    void handle_get(http_request request) {
        ucout << "GET request received" << std::endl;

        // Call the function associated with the route
        auto response_message = hello();
        
        // Create a JSON response
        json::value response_data;
        response_data[U("message")] = json::value::string(response_message);

        // Send response
        request.reply(status_codes::OK, response_data).then([](pplx::task<void> t) {
            try {
                t.get();
            } catch (const std::exception& e) {
                std::cerr << "Error sending response: " << e.what() << std::endl;
            }
        }).wait();
    }

    // Function that returns the message to display
    std::string hello() {
        return "Hello, welcome to the web application!";
    }
};

int main() {
    uri uri(U("http://localhost:8080"));
    WebApplication app(uri);

    app.open();

    std::string line;
    std::cout << "Press Enter to exit." << std::endl;
    std::getline(std::cin, line);

    return 0;
}
