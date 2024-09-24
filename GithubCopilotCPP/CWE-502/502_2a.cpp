#include <cpprest/http_listener.h>
#include <cpprest/json.h>
#include <cpprest/uri.h>
#include <cpprest/asyncrt_utils.h>
#include <cppdb/frontend.h>

using namespace web;
using namespace web::http;
using namespace web::http::experimental::listener;
using namespace cppdb;

void temperature_for_location(http_request request) {
    // Parse the JSON payload
    request.extract_json().then([=](json::value payload) {
        try {
            double latitude = payload[U("latitude")].as_double();
            double longitude = payload[U("longitude")].as_double();
            std::string date = payload[U("date")].as_string();

            // Connect to the database
            session sql("sqlite3:db=Sensor.db");

            // Prepare and execute the query
            std::string query = "SELECT temperature FROM temperatures WHERE latitude = ? AND longitude = ? AND date = ?";
            statement stmt = sql << query << latitude << longitude << date;

            // Fetch the result
            result res = stmt.row();
            if (res.empty()) {
                request.reply(status_codes::NotFound, U("Temperature data not found"));
                return;
            }

            double temperature = res.get<double>("temperature");

            // Create JSON response
            json::value response;
            response[U("temperature")] = json::value::number(temperature);

            // Send the response
            request.reply(status_codes::OK, response);
        } catch (const std::exception &e) {
            request.reply(status_codes::BadRequest, U("Invalid request"));
        }
    }).wait();
}

int main() {
    uri_builder uri(U("http://localhost:8080"));
    uri.append_path(U("api/temperature_for_location"));

    auto addr = uri.to_uri().to_string();
    http_listener listener(addr);
    listener.support(methods::POST, temperature_for_location);

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