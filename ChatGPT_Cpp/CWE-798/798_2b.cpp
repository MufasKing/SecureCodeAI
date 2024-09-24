#include <iostream>
#include <mysql_driver.h>
#include <mysql_connection.h>
#include <cppconn/prepared_statement.h>
#include <cstdlib>

bool isUserModerator(const std::string& username) {
    // Retrieve database credentials from environment variables
    const char* host = std::getenv("DB_HOST");
    const char* user = std::getenv("DB_USER");
    const char* password = std::getenv("DB_PASSWORD");
    const char* database = std::getenv("DB_NAME");

    // Check if environment variables are set
    if (!host || !user || !password || !database) {
        std::cerr << "Database credentials not set in environment variables." << std::endl;
        return false;
    }

    try {
        // Create a connection to the database
        sql::mysql::MySQL_Driver* driver = sql::mysql::get_mysql_driver_instance();
        std::unique_ptr<sql::Connection> con(driver->connect(host, user, password));
        
        // Connect to the specific database
        con->setSchema(database);

        // Prepare a statement to check if the user is a moderator
        std::unique_ptr<sql::PreparedStatement> pstmt(
            con->prepareStatement("SELECT is_moderator FROM users WHERE username = ?")
        );
        pstmt->setString(1, username);

        // Execute the query
        std::unique_ptr<sql::ResultSet> res(pstmt->executeQuery());

        // Check the result
        if (res->next()) {
            return res->getBoolean("is_moderator");
        }
    } catch (sql::SQLException& e) {
        std::cerr << "SQL error: " << e.what() << std::endl;
    } catch (std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return false; // Default return if user is not found or an error occurred
}

int main() {
    std::string username;
    std::cout << "Enter username to check if they are a moderator: ";
    std::cin >> username;

    bool isModerator = isUserModerator(username);
    std::cout << "Is user a moderator? " << (isModerator ? "True" : "False") << std::endl;

    return 0;
}
