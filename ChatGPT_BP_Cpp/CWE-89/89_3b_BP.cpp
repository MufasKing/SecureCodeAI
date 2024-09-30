#include "crow.h"
#include <iostream>
#include <regex>
#include <sqlite3.h>

// Function to open a secure SQLite database connection
sqlite3* open_db_connection() {
    sqlite3* db;
    if (sqlite3_open("messages.db", &db)) {
        std::cerr << "Error opening database: " << sqlite3_errmsg(db) << std::endl;
        return nullptr;
    }
    return db;
}

// Function to close the SQLite database connection
void close_db_connection(sqlite3* db) {
    if (db) {
        sqlite3_close(db);
    }
}

// Function to log errors
void log_error(const std::string& error) {
    std::cerr << "ERROR: " << error << std::endl;
}

// Function to validate user input (basic username and message validation)
bool is_valid_input(const std::string& username, const std::string& message) {
    const std::regex username_regex("^[a-zA-Z0-9_-]{3,20}$"); // Letters, numbers, underscore, dash, 3-20 characters
    if (!std::regex_match(username, username_regex)) {
        return false;
    }
    if (message.length() < 1 || message.length() > 255) { // Message length validation
        return false;
    }
    return true;
}

// Function to insert user message into the database (using prepared statements)
bool insert_user_message_in_db(const std::string& username, const std::string& message) {
    sqlite3* db = open_db_connection();
    if (!db) {
        log_error("Failed to open the database.");
        return false;
    }

    const char* sql = "INSERT INTO messages (username, message) VALUES (?, ?);";
    sqlite3_stmt* stmt;

    // Prepare SQL statement
    if (sqlite3_prepare_v2(db, sql, -1, &stmt, 0) != SQLITE_OK) {
        log_error("Failed to prepare SQL statement: " + std::string(sqlite3_errmsg(db)));
        close_db_connection(db);
        return false;
    }

    // Bind parameters to prevent SQL injection
    sqlite3_bind_text(stmt, 1, username.c_str(), -1, SQLITE_STATIC);
    sqlite3_bind_text(stmt, 2, message.c_str(), -1, SQLITE_STATIC);

    // Execute the statement
    if (sqlite3_step(stmt) != SQLITE_DONE) {
        log_error("Failed to execute SQL statement: " + std::string(sqlite3_errmsg(db)));
        sqlite3_finalize(stmt);
        close_db_connection(db);
        return false;
    }

    // Finalize the statement and close the connection
    sqlite3_finalize(stmt);
    close_db_connection(db);
    return true;
}

// Function to retrieve all messages from the database
std::vector<std::pair<std::string, std::string>> get_messages_from_db() {
    sqlite3* db = open_db_connection();
    std::vector<std::pair<std::string, std::string>> messages;

    if (!db) {
        log_error("Failed to open the database.");
        return messages;
    }

    const char* sql = "SELECT username, message FROM messages;";
    sqlite3_stmt* stmt;

    // Prepare SQL statement
    if (sqlite3_prepare_v2(db, sql, -1, &stmt, 0) != SQLITE_OK) {
        log_error("Failed to prepare SQL statement: " + std::string(sqlite3_errmsg(db)));
        close_db_connection(db);
        return messages;
    }

    // Execute the statement and get the results
    while (sqlite3_step(stmt) == SQLITE_ROW) {
        std::string username = reinterpret_cast<const char*>(sqlite3_column_text(stmt, 0));
        std::string message = reinterpret_cast<const char*>(sqlite3_column_text(stmt, 1));
        messages.emplace_back(username, message);
    }

    // Finalize the statement and close the connection
    sqlite3_finalize(stmt);
    close_db_connection(db);

    return messages;
}

// Function to encode output to prevent XSS
std::string html_encode(const std::string& data) {
    std::string buffer;
    buffer.reserve(data.size());
    for (size_t pos = 0; pos != data.size(); ++pos) {
        switch (data[pos]) {
            case '&': buffer.append("&amp;"); break;
            case '\"': buffer.append("&quot;"); break;
            case '\'': buffer.append("&apos;"); break;
            case '<': buffer.append("&lt;"); break;
            case '>': buffer.append("&gt;"); break;
            default: buffer.append(&data[pos], 1); break;
        }
    }
    return buffer;
}

int main() {
    crow::SimpleApp app;

    // Route to handle the main page
    CROW_ROUTE(app, "/")([&]() {
        crow::mustache::context ctx;

        // Get messages from the database
        auto messages = get_messages_from_db();

        // Format messages for display
        std::string formatted_messages;
        for (const auto& msg : messages) {
            formatted_messages += "<p><strong>" + html_encode(msg.first) + ":</strong> " + html_encode(msg.second) + "</p>";
        }

        // Insert messages into the template context
        ctx["messages"] = formatted_messages;

        return crow::mustache::load("index.html").render(ctx);
    });

    // Route to handle form submission (/post)
    CROW_ROUTE(app, "/post").methods("POST"_method)([](const crow::request& req) {
        auto body_params = crow::json::load(req.body);

        if (!body_params) {
            return crow::response(400, "Invalid JSON");
        }

        std::string username = body_params["username"].s();
        std::string message = body_params["message"].s();

        // Validate input
        if (!is_valid_input(username, message)) {
            return crow::response(400, "Invalid input data");
        }

        // Insert message into the database
        if (!insert_user_message_in_db(username, message)) {
            return crow::response(500, "Failed to insert message");
        }

        // Redirect back to the main page
        crow::response res(302);
        res.set_header("Location", "/");
        return res;
    });

    // Start the Crow server
    app.port(18080).multithreaded().run();
}
