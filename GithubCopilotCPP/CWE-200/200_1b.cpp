#include <iostream>
#include <string>
#include <cpprest/http_listener.h>
#include <cpprest/json.h>
#include <cpprest/uri.h>
#include <cpprest/asyncrt_utils.h>
#include <sqlite3.h>

using namespace web;
using namespace web::http;
using namespace web::http::experimental::listener;

void handle_login(http_request request) {
    auto queries = uri::split_query(request.request_uri().query());
    auto username = queries[U("username")];
    auto password = queries[U("password")];

    sqlite3* db;
    sqlite3_open("database.db", &db);

    std::string sql = "SELECT COUNT(*) FROM users WHERE username = ? AND password = ?";
    sqlite3_stmt* stmt;
    sqlite3_prepare_v2(db, sql.c_str(), -1, &stmt, nullptr);
    sqlite3_bind_text(stmt, 1, username.c_str(), -1, SQLITE_STATIC);
    sqlite3_bind_text(stmt, 2, password.c_str(), -1, SQLITE_STATIC);

    int count = 0;
    if (sqlite3_step(stmt) == SQLITE_ROW) {
        count = sqlite3_column_int(stmt, 0);
    }

    sqlite3_finalize(stmt);
    sqlite3_close(db);

    if (count > 0) {
        request.reply(status_codes::Found, U("Redirecting to home page"), { { U("Location"), U("/home") } });
    } else {
        request.reply(status_codes::Found, U("Redirecting to login page"), { { U("Location"), U("/login") } });
    }
}

int main() {
    http_listener listener(U("http://localhost:8080/login"));
    listener.support(methods::POST, handle_login);

    try {
        listener
            .open()
            .then([&listener]() { std::wcout << L"Starting to listen at: " << listener.uri().to_string() << std::endl; })
            .wait();

        std::string line;
        std::getline(std::cin, line);
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}