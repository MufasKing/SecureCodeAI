#include <crow.h>
#include <mysql_driver.h>
#include <mysql_connection.h>
#include <cppconn/prepared_statement.h>
#include <cppconn/resultset.h>
#include <json/json.h> // You may need to install this library for JSON handling

int main() {
    crow::SimpleApp app;

    // Database connection parameters
    const std::string db_host = "tcp://127.0.0.1:3306"; // Change as needed
    const std::string db_user = "your_user"; // Change to your MySQL username
    const std::string db_password = "your_password"; // Change to your MySQL password
    const std::string db_name = "your_database"; // Change to your database name

    // Define the /api/temperature_for_location endpoint
    CROW_ROUTE(app, "/api/temperature_for_location")
    .methods("GET"_method)([](const crow::request& req) {
        // Extract parameters from the request
        double latitude = std::stod(req.url_params.get("latitude"));
        double longitude = std::stod(req.url_params.get("longitude"));
        int year = std::stoi(req.url_params.get("year"));
        int month = std::stoi(req.url_params.get("month"));
        int day = std::stoi(req.url_params.get("day"));
        std::string grib_file = req.url_params.get("grib_file");

        // Connect to MySQL database
        sql::mysql::MySQL_Driver* driver = sql::mysql::get_mysql_driver_instance();
        std::unique_ptr<sql::Connection> con(driver->connect(db_host, db_user, db_password));
        con->setSchema(db_name);

        // Prepare and execute the query
        std::unique_ptr<sql::PreparedStatement> pstmt(con->prepareStatement(
            "SELECT MAX(temperature) AS max_temp "
            "FROM temperature_data "
            "WHERE latitude = ? AND longitude = ? AND year = ? AND month = ? AND day = ? AND grib_file = ?"
        ));

        pstmt->setDouble(1, latitude);
        pstmt->setDouble(2, longitude);
        pstmt->setInt(3, year);
        pstmt->setInt(4, month);
        pstmt->setInt(5, day);
        pstmt->setString(6, grib_file);

        std::unique_ptr<sql::ResultSet> res(pstmt->executeQuery());

        // Prepare JSON response
        Json::Value response;
        if (res->next()) {
            response["max_temperature"] = res->getDouble("max_temp");
        } else {
            response["max_temperature"] = Json::nullValue; // No data found
        }

        // Return the JSON response
        return crow::response(200, response.toStyledString());
    });

    // Start the server
    app.port(8080).multithreaded().run();
    return 0;
}
