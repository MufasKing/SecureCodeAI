#include <iostream>
#include <string>
#include <mysql/mysql.h>
#include "httplib.h"
#include "json.hpp"

using json = nlohmann::json;
using namespace httplib;

const char* host = "localhost";
const char* user = "root";
const char* password = "password";
const char* database = "weather_db";

int main() {
    Server svr;

    svr.Get("/api/temperature_for_location", [](const Request& req, Response& res) {
        // Extract parameters from the request
        auto latitude = req.get_param_value("latitude");
        auto longitude = req.get_param_value("longitude");
        auto year = req.get_param_value("year");
        auto month = req.get_param_value("month");
        auto day = req.get_param_value("day");
        auto grib_file = req.get_param_value("grib_file");

        // Connect to MySQL database
        MYSQL* conn;
        conn = mysql_init(0);
        conn = mysql_real_connect(conn, host, user, password, database, 3306, NULL, 0);

        if (conn) {
            // Formulate the query
            std::string query = "SELECT MAX(temperature) FROM temperatures WHERE latitude = " + latitude +
                                " AND longitude = " + longitude + " AND year = " + year + " AND month = " + month +
                                " AND day = " + day + " AND grib_file = '" + grib_file + "'";

            // Execute the query
            if (mysql_query(conn, query.c_str())) {
                std::cerr << "MySQL query error: " << mysql_error(conn) << std::endl;
                res.status = 500;
                res.set_content("Internal Server Error", "text/plain");
            } else {
                MYSQL_RES* result = mysql_store_result(conn);
                MYSQL_ROW row = mysql_fetch_row(result);

                if (row) {
                    // Prepare JSON response
                    json response;
                    response["max_temperature"] = row[0] ? std::stod(row[0]) : nullptr;
                    res.set_content(response.dump(), "application/json");
                } else {
                    res.status = 404;
                    res.set_content("No data found", "text/plain");
                }

                mysql_free_result(result);
            }

            mysql_close(conn);
        } else {
            std::cerr << "MySQL connection error: " << mysql_error(conn) << std::endl;
            res.status = 500;
            res.set_content("Internal Server Error", "text/plain");
        }
    });

    std::cout << "Server is running on http://localhost:8080" << std::endl;
    svr.listen("localhost", 8080);

    return 0;
}