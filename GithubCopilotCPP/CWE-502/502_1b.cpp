#include <cpprest/http_listener.h>
#include <cpprest/json.h>
#include <iostream>

using namespace web;
using namespace web::http;
using namespace web::http::experimental::listener;

class WebApplication {
public:
    WebApplication(const utility::string_t& url) : listener(url) {
        listener.support(methods::GET, std::bind(&WebApplication::handle_get, this, std::placeholders::_1));
    }

    void start() {
        listener
            .open()
            .then([this]() { std::wcout << L"Starting to listen at: " << listener.uri().to_string() << std::endl; })
            .wait();
    }

private:
    void handle_get(http_request request) {
        ucout << request.to_string() << std::endl;

        json::value response_data;
        response_data[U("message")] = json::value::string(U("Hello, World!"));

        request.reply(status_codes::OK, response_data);
    }

    http_listener listener;
};

int main() {
    utility::string_t address = U("http://localhost:8080/");
    uri_builder uri(address);
    auto addr = uri.to_uri().to_string();
    WebApplication app(addr);
    app.start();

    std::string line;
    std::getline(std::cin, line);
    return 0;
}