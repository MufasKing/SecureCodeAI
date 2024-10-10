#include "crow.h"
#include <sqlite3.h>
#include <iostream>
#include <sstream>

// Function to execute a query and return the result as a string
std::string executeQuery(const std::string& query) {
    sqlite3* db;
    sqlite3_stmt* stmt;
    std::ostringstream result;

    // Open the database
    if (sqlite3_open("example.db", &db) != SQLITE_OK) {
        return "Failed to open database";
    }

    // Prepare the SQL statement
    if (sqlite3_prepare_v2(db, query.c_str(), -1, &stmt, nullptr) != SQLITE_OK) {
        sqlite3_close(db);
        return "Failed to prepare statement";
    }

    // Execute the query and process the result
    while (sqlite3_step(stmt) == SQLITE_ROW) {
        for (int i = 0; i < sqlite3_column_count(stmt); ++i) {
            result << sqlite3_column_text(stmt, i) << " ";
        }
        result << "\n";
    }

    // Clean up
    sqlite3_finalize(stmt);
    sqlite3_close(db);

    return result.str();
}

int main() {
    crow::SimpleApp app;

    // Define a route
    CROW_ROUTE(app, "/query")
    ([]() {
        // Define the query
        std::string query = "SELECT * FROM example_table";

        // Execute the query and get the result
        std::string result = executeQuery(query);

        // Return the result as the response
        return crow::response(result);
    });

    // Start the Crow application
    app.port(8080).multithreaded().run();

    return 0;
}