#include <cpprest/http_listener.h>
#include <cpprest/json.h>
#include <cpprest/uri.h>
#include <cpprest/asyncrt_utils.h>
#include <iostream>
#include <vector>
#include <string>

// Function to insert user message into the database
void insert_user_message_in_db(const std::string& username, const std::string& message) {
    // Database insertion logic here
}

// Function to retrieve all messages from the database
std::vector<std::pair<std::string, std::string>> get_all_messages_from_db() {
    // Database retrieval logic here
    return {}; // Placeholder return
}

void handle_post(web::http::http_request request) {
    request.extract_json().then([=](web::json::value json) {
        auto username = json[U("username")].as_string();
        auto message = json[U("message")].as_string();
        insert_user_message_in_db(username, message);
        request.reply(web::http::status_codes::Found, U(""), { { U("Location"), U("/") } });
    }).wait();
}

void handle_get(web::http::http_request request) {
    auto messages = get_all_messages_from_db();
    web::json::value response = web::json::value::array();
    int i = 0;
    for (const auto& msg : messages) {
        web::json::value message;
        message[U("username")] = web::json::value::string(msg.first);
        message[U("message")] = web::json::value::string(msg.second);
        response[i++] = message;
    }
    request.reply(web::http::status_codes::OK, response);
}

int main() {
    web::http::experimental::listener::http_listener listener(U("http://localhost:8080"));

    listener.support(web::http::methods::POST, handle_post);
    listener.support(web::http::methods::GET, handle_get);

    try {
        listener
            .open()
            .then([&listener]() { std::wcout << L"Starting to listen at: " << listener.uri().to_string() << std::endl; })
            .wait();

        std::string line;
        std::getline(std::cin, line);
    }
    catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}