#include <crow.h>
#include <sqlite3.h>
#include <nlohmann/json.hpp>
#include <iostream>
#include <string>

using json = nlohmann::json;

// Function to fetch temperature from the database
double get_temperature(double latitude, double longitude, const std::string& date) {
    sqlite3* db;
    sqlite3_stmt* stmt;
    double temperature = 0.0;

    // Open the database
    if (sqlite3_open("Sensor.db", &db) != SQLITE_OK) {
        std::cerr << "Can't open database: " << sqlite3_errmsg(db) << std::endl;
        return temperature;
    }

    // Prepare the SQL statement
    const char* sql = "SELECT temperature FROM TemperatureData WHERE latitude = ? AND longitude = ? AND date = ?";
    if (sqlite3_prepare_v2(db, sql, -1, &stmt, nullptr) != SQLITE_OK) {
        std::cerr << "Failed to prepare statement: " << sqlite3_errmsg(db) << std::endl;
        sqlite3_close(db);
        return temperature;
    }

    // Bind parameters
    sqlite3_bind_double(stmt, 1, latitude);
    sqlite3_bind_double(stmt, 2, longitude);
    sqlite3_bind_text(stmt, 3, date.c_str(), -1, SQLITE_STATIC);

    // Execute the statement and fetch the temperature
    if (sqlite3_step(stmt) == SQLITE_ROW) {
        temperature = sqlite3_column_double(stmt, 0);
    } else {
        std::cerr << "No data found for the given parameters." << std::endl;
    }

    // Clean up
    sqlite3_finalize(stmt);
    sqlite3_close(db);
    
    return temperature;
}

int main() {
    crow::App app;

    app.post("/api/temperature_for_location", [](const crow::request& req) {
        auto json_data = json::parse(req.body);
        double latitude = json_data["latitude"];
        double longitude = json_data["longitude"];
        std::string date = json_data["date"];

        double temperature = get_temperature(latitude, longitude, date);

        json response;
        response["temperature"] = temperature;

        return crow::response{response.dump()};
    });

    app.port(8080).multithreaded().run();
}
