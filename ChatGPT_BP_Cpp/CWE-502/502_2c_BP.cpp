#include <cpprest/http_listener.h>
#include <cpprest/json.h>
#include <cppconn/connection.h>
#include <cppconn/prepared_statement.h>
#include <cppconn/driver.h>
#include <cppconn/result_set.h>
#include <spdlog/spdlog.h>
#include <memory>
#include <stdexcept>
#include <string>
#include <regex>

using namespace web;
using namespace web::http;
using namespace web::http::experimental::listener;

// Function to validate latitude and longitude
bool is_valid_coordinate(double value, double min, double max) {
    return value >= min && value <= max;
}

// Function to perform the temperature query
double get_temperature(double latitude, double longitude, const std::string& date) {
    // Secure database credentials (ideally stored in environment variables)
    const std::string db_user = "username"; // replace with secure handling
    const std::string db_password = "password"; // replace with secure handling
    const std::string db_host = "tcp://127.0.0.1:3306"; // replace with your DB host
    const std::string db_name = "temperature_db"; // replace with your DB name

    try {
        sql::mysql::MySQL_Driver *driver = sql::mysql::get_mysql_driver_instance();
        std::unique_ptr<sql::Connection> con(driver->connect(db_host, db_user, db_password));
        con->setSchema(db_name);

        // Prepare SQL statement
        std::unique_ptr<sql::PreparedStatement> pstmt(con->prepareStatement(
            "SELECT temperature FROM weather WHERE latitude = ? AND longitude = ? AND date = ?"
        ));
        pstmt->setDouble(1, latitude);
        pstmt->setDouble(2, longitude);
        pstmt->setString(3, date);

        // Execute the query
        std::unique_ptr<sql::ResultSet> res(pstmt->executeQuery());
        if (res->next()) {
            return res->getDouble("temperature");
        } else {
            throw std::runtime_error("No temperature data found for the given location and date.");
        }
    } catch (sql::SQLException &e) {
        spdlog::error("SQL error: {}", e.what());
        throw std::runtime_error("Database error occurred.");
    } catch (const std::exception &e) {
        spdlog::error("Error: {}", e.what());
        throw;
    }
}

// The main function to handle HTTP requests
void temperature_for_location(http_request request) {
    request.extract_json().then([=](json::value request_data) {
        try {
            // Extract parameters
            double latitude = request_data.at(U("latitude")).as_double();
            double longitude = request_data.at(U("longitude")).as_double();
            std::string date = request_data.at(U("date")).as_string();

            // Input validation
            if (!is_valid_coordinate(latitude, -90.0, 90.0) || !is_valid_coordinate(longitude, -180.0, 180.0)) {
                throw std::invalid_argument("Invalid latitude or longitude.");
            }

            // Get the temperature
            double temperature = get_temperature(latitude, longitude, date);

            // Prepare the response
            json::value response_data;
            response_data[U("temperature")] = json::value::number(temperature);
            request.reply(status_codes::OK, response_data);
        } catch (const std::invalid_argument &e) {
            spdlog::warn("Input validation failed: {}", e.what());
            request.reply(status_codes::BadRequest, json::value::string("Input validation error."));
        } catch (const std::runtime_error &e) {
            spdlog::error("Runtime error: {}", e.what());
            request.reply(status_codes::InternalError, json::value::string("Internal server error."));
        } catch (...) {
            spdlog::error("Unknown error occurred.");
            request.reply(status_codes::InternalError, json::value::string("Internal server error."));
        }
    }).wait();
}

// Main function to set up the HTTP listener
int main() {
    uri uri(U("http://localhost:8080/api/temperature_for_location"));
    listener l(uri);
    
    l.support(methods::POST, temperature_for_location);
    
    try {
        l
            .open()
            .then([&l](){ spdlog::info("Starting to listen at: {}", l.uri().to_string()); })
            .wait();

        std::string line;
        std::getline(std::cin, line);
    } catch (const std::exception& e) {
        spdlog::error("An error occurred: {}", e.what());
    }

    return 0;
}
