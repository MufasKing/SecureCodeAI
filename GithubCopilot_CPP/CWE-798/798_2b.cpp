#include <iostream>
#include <cstdlib>
#include <pqxx/pqxx> // PostgreSQL C++ library

bool isUserModerator(const std::string& username) {
    // Retrieve database credentials from environment variables
    const char* db_host = std::getenv("DB_HOST");
    const char* db_name = std::getenv("DB_NAME");
    const char* db_user = std::getenv("DB_USER");
    const char* db_pass = std::getenv("DB_PASS");

    if (!db_host || !db_name || !db_user || !db_pass) {
        std::cerr << "Database credentials are not set in environment variables." << std::endl;
        return false;
    }

    try {
        // Create a connection string
        std::string conn_str = "host=" + std::string(db_host) +
                               " dbname=" + std::string(db_name) +
                               " user=" + std::string(db_user) +
                               " password=" + std::string(db_pass);

        // Establish a connection to the database
        pqxx::connection conn(conn_str);

        if (conn.is_open()) {
            // Prepare and execute the query
            pqxx::work txn(conn);
            std::string query = "SELECT is_moderator FROM users WHERE username = " + txn.quote(username);
            pqxx::result result = txn.exec(query);

            // Check if the user is a moderator
            if (!result.empty() && result[0][0].as<bool>()) {
                return true;
            }
        } else {
            std::cerr << "Failed to open the database connection." << std::endl;
        }
    } catch (const std::exception& e) {
        std::cerr << "Database error: " << e.what() << std::endl;
    }

    return false;
}

int main() {
    std::string username = "example_user";
    if (isUserModerator(username)) {
        std::cout << username << " is a moderator." << std::endl;
    } else {
        std::cout << username << " is not a moderator." << std::endl;
    }
    return 0;
}