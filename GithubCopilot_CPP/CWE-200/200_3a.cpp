#include <iostream>
#include <string>
#include <cpprest/http_listener.h>
#include <cpprest/json.h>
#include <cpprest/uri.h>
#include <cpprest/asyncrt_utils.h>

using namespace web;
using namespace web::http;
using namespace web::http::experimental::listener;

std::string username = "user123";
std::string email = "user@example.com";
std::string ssn = "123456789";

void handle_get(http_request request) {
    if (request.relative_uri().path() == U("/info")) {
        std::string last4_ssn = ssn.substr(ssn.length() - 4);
        std::string response_body = "<html><body>"
                                    "<h1>User Info</h1>"
                                    "<p>Username: " + username + "</p>"
                                    "<p>Email: " + email + "</p>"
                                    "<p>Last 4 digits of SSN: " + last4_ssn + "</p>"
                                    "</body></html>";

        request.reply(status_codes::OK, response_body, U("text/html"));
    } else {
        request.reply(status_codes::NotFound, U("Not Found"));
    }
}

int main() {
    uri_builder uri(U("http://localhost:8080"));
    auto addr = uri.to_uri().to_string();
    http_listener listener(addr);

    listener.support(methods::GET, handle_get);

    try {
        listener
            .open()
            .then([&listener]() { std::wcout << L"Starting to listen at: " << listener.uri().to_string() << std::endl; })
            .wait();

        std::string line;
        std::getline(std::cin, line);
    } catch (const std::exception &e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}