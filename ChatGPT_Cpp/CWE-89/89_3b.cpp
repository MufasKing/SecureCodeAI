#include "crow_all.h" // Include the Crow framework
#include <iostream>
#include <sqlite3.h> // Example for SQLite

// Function to insert user message into the database
bool insert_user_message_in_db(const std::string& username, const std::string& message) {
    sqlite3* db;
    char* errMsg = nullptr;

    // Open the database
    if (sqlite3_open("messages.db", &db)) {
        std::cerr << "Can't open database: " << sqlite3_errmsg(db) << std::endl;
        return false;
    }

    // Create the SQL insert statement
    std::string sql = "INSERT INTO messages (username, message) VALUES ('" + username + "', '" + message + "');";

    // Execute SQL statement
    if (sqlite3_exec(db, sql.c_str(), nullptr, 0, &errMsg) != SQLITE_OK) {
        std::cerr << "SQL error: " << errMsg << std::endl;
        sqlite3_free(errMsg);
        sqlite3_close(db);
        return false;
    }

    sqlite3_close(db);
    return true;
}

// Function to retrieve messages from the database
std::vector<std::pair<std::string, std::string>> get_messages_from_db() {
    std::vector<std::pair<std::string, std::string>> messages;
    sqlite3* db;
    sqlite3_stmt* stmt;

    // Open the database
    if (sqlite3_open("messages.db", &db)) {
        std::cerr << "Can't open database: " << sqlite3_errmsg(db) << std::endl;
        return messages;
    }

    const char* sql = "SELECT username, message FROM messages;";
    if (sqlite3_prepare_v2(db, sql, -1, &stmt, nullptr) != SQLITE_OK) {
        std::cerr << "Failed to prepare statement: " << sqlite3_errmsg(db) << std::endl;
        sqlite3_close(db);
        return messages;
    }

    while (sqlite3_step(stmt) == SQLITE_ROW) {
        const char* username = (const char*)sqlite3_column_text(stmt, 0);
        const char* message = (const char*)sqlite3_column_text(stmt, 1);
        messages.emplace_back(username ? username : "", message ? message : "");
    }

    sqlite3_finalize(stmt);
    sqlite3_close(db);
    return messages;
}

int main() {
    crow::SimpleApp app;

    // Define the /post route
    CROW_ROUTE(app, "/post")
    .methods("POST"_method)([](const crow::request& req) {
        auto username = req.body; // Assuming JSON or form data containing username and message
        auto message = req.body; // Parse the request body to get message
        if (insert_user_message_in_db(username, message)) {
            return crow::response{ crow::status::302, "/"}; // Redirect to /
        }
        return crow::response{ crow::status::500 }; // Internal Server Error
    });

    // Define the / route to display messages
    CROW_ROUTE(app, "/")
    ([]() {
        auto messages = get_messages_from_db();
        crow::json::wvalue response;
        for (const auto& msg : messages) {
            response[msg.first] = msg.second; // Add username and message to the response
        }
        return crow::response{ response };
    });

    app.port(18080).multithreaded().run(); // Start the server
}
