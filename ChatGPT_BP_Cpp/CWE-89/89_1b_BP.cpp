#include <cpprest/http_listener.h>
#include <cpprest/json.h>
#include <cpprest/uri.h>
#include <mysql_driver.h>
#include <mysql_connection.h>
#include <cppconn/prepared_statement.h>
#include <cppconn/resultset.h>
#include <regex>
#include <stdexcept>
#include <iostream>

using namespace web;
using namespace web::http;
using namespace web::http::experimental::listener;
using namespace sql;
using namespace std;

// Constants for DB Connection
const std::string DB_HOST = "tcp://127.0.0.1:3306";
const std::string DB_USER = "root";
const std::string DB_PASS = "password";
const std::string DB_NAME = "subscriptions";

// Input validation for email
bool is_valid_email(const std::string& email) {
    const std::regex pattern(R"((\w+)(\.{1}\w+)*@(\w+)(\.\w{2,})+)");
    return regex_match(email, pattern);
}

// Database connection creation
std::shared_ptr<Connection> get_db_connection() {
    sql::mysql::MySQL_Driver *driver;
    std::shared_ptr<Connection> con;

    try {
        driver = sql::mysql::get_mysql_driver_instance();
        con = std::shared_ptr<Connection>(driver->connect(DB_HOST, DB_USER, DB_PASS));
        con->setSchema(DB_NAME);
    } catch (sql::SQLException &e) {
        cerr << "Error connecting to the database: " << e.what() << endl;
        throw std::runtime_error("Database connection error");
    }

    return con;
}

// Unsubscribe logic
void unsubscribe_user(const std::string& email, http_response& response) {
    if (!is_valid_email(email)) {
        response.set_status_code(status_codes::BadRequest);
        response.set_body(U("Invalid email format."));
        return;
    }

    std::shared_ptr<Connection> con;
    std::shared_ptr<PreparedStatement> pstmt;
    std::shared_ptr<ResultSet> res;

    try {
        con = get_db_connection();

        // Check if the email exists in the database
        pstmt = std::shared_ptr<PreparedStatement>(con->prepareStatement("SELECT email FROM users WHERE email = ?"));
        pstmt->setString(1, email);
        res = std::shared_ptr<ResultSet>(pstmt->executeQuery());

        if (!res->next()) {
            // Email not found
            response.set_status_code(status_codes::NotFound);
            response.set_body(U("User is not subscribed."));
            return;
        }

        // Email found, unsubscribe the user (delete user from the table)
        pstmt = std::shared_ptr<PreparedStatement>(con->prepareStatement("DELETE FROM users WHERE email = ?"));
        pstmt->setString(1, email);
        pstmt->executeUpdate();

        response.set_status_code(status_codes::OK);
        response.set_body(U("Successfully unsubscribed."));
    } catch (sql::SQLException &e) {
        cerr << "SQL Error: " << e.what() << endl;
        response.set_status_code(status_codes::InternalError);
        response.set_body(U("Internal server error."));
    } catch (std::exception &e) {
        cerr << "Error: " << e.what() << endl;
        response.set_status_code(status_codes::InternalError);
        response.set_body(U("An error occurred."));
    }
}

// Endpoint handler
void handle_get(http_request request) {
    auto query_params = uri::split_query(request.request_uri().query());

    if (query_params.find(U("email")) == query_params.end()) {
        request.reply(status_codes::BadRequest, U("Email parameter is missing."));
        return;
    }

    auto email = query_params[U("email")];
    http_response response;

    unsubscribe_user(email, response);

    request.reply(response);
}

// Main function
int main() {
    http_listener listener(U("http://localhost:8080/unsubscribe"));

    listener.support(methods::GET, handle_get);

    try {
        listener
            .open()
            .then([&listener]() { std::cout << "Starting to listen at: " << listener.uri().to_string() << std::endl; })
            .wait();

        std::cout << "Press ENTER to stop the listener." << std::endl;
        std::string line;
        std::getline(std::cin, line);
    } catch (const std::exception& e) {
        std::cerr << "Error occurred: " << e.what() << std::endl;
    }

    return 0;
}
