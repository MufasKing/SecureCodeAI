#include <cpprest/http_listener.h>
#include <cpprest/json.h>
#include <iostream>
#include <string>

using namespace web;
using namespace web::http;
using namespace web::http::experimental::listener;

class MyServer {
public:
    MyServer() {
        listener = http_listener(U("http://localhost:8080"));

        listener.support(methods::GET, std::bind(&MyServer::handle_get, this, std::placeholders::_1));
        listener.support(methods::POST, std::bind(&MyServer::handle_post, this, std::placeholders::_1));
    }

    void open() {
        listener
            .open()
            .then([this](){ std::wcout << L"Starting to listen at: " << listener.uri().to_string() << std::endl; })
            .wait();
    }

    void handle_get(http_request request) {
        auto path = request.request_uri().path();

        if (path == U("/login")) {
            login(request);
        } else if (path == U("/index")) {
            index(request);
        } else if (path == U("/user_page")) {
            user_page(request);
        } else if (path == U("/admin_page")) {
            admin_page(request);
        } else {
            request.reply(status_codes::NotFound, U("Not Found"));
        }
    }

    void handle_post(http_request request) {
        auto path = request.request_uri().path();

        if (path == U("/do_login")) {
            do_login(request);
        } else {
            request.reply(status_codes::NotFound, U("Not Found"));
        }
    }

private:
    http_listener listener;

    void login(http_request request) {
        json::value response_data;
        response_data[U("message")] = json::value::string(U("Login Page"));
        request.reply(status_codes::OK, response_data);
    }

    void do_login(http_request request) {
        request.extract_json().then([=](json::value json_data) {
            // Here, you would typically handle the login logic, e.g., validate user credentials
            json::value response_data;
            response_data[U("message")] = json::value::string(U("Logged in successfully"));
            request.reply(status_codes::OK, response_data);
        }).wait();
    }

    void index(http_request request) {
        json::value response_data;
        response_data[U("message")] = json::value::string(U("Welcome to the Index Page"));
        request.reply(status_codes::OK, response_data);
    }

    void user_page(http_request request) {
        json::value response_data;
        response_data[U("message")] = json::value::string(U("Welcome to the User Page"));
        request.reply(status_codes::OK, response_data);
    }

    void admin_page(http_request request) {
        json::value response_data;
        response_data[U("message")] = json::value::string(U("Welcome to the Admin Page"));
        request.reply(status_codes::OK, response_data);
    }
};

int main() {
    MyServer server;
    server.open();

    std::string line;
    std::getline(std::cin, line); // Keep the server running
    return 0;
}
