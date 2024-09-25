#include <cpprest/http_listener.h>
#include <cpprest/json.h>
#include <iostream>

using namespace web;
using namespace web::http;
using namespace web::http::experimental::listener;

void handle_get(http_request request) {
    ucout << request.to_string() << std::endl;
    json::value response_data;
    response_data[U("message")] = json::value::string(U("Hello, World!"));
    request.reply(status_codes::OK, response_data);
}

int main() {
    http_listener listener(U("http://localhost:8080"));

    listener.support(methods::GET, handle_get);

    try {
        listener
            .open()
            .then([&listener]() { ucout << "Starting to listen at: " << listener.uri().to_string() << std::endl; })
            .wait();

        std::string line;
        std::getline(std::cin, line);
    } catch (const std::exception &e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}