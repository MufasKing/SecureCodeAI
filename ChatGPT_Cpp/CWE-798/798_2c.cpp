#include <iostream>
#include <mysql_driver.h>
#include <mysql_connection.h>

bool doesUserExist(const std::string& username) {
    // Create a connection to the database
    sql::mysql::MySQL_Driver* driver;
    sql::Connection* con;

    try {
        // Initialize MySQL driver
        driver = sql::mysql::get_mysql_driver_instance();
        con = driver->connect("tcp://127.0.0.1:3306", "your_username", "your_password"); // Update with your database credentials

        // Connect to the database
        con->setSchema("your_database_name"); // Update with your database name

        // Prepare and execute the SQL query
        std::unique_ptr<sql::PreparedStatement> pstmt(con->prepareStatement("SELECT COUNT(*) FROM users WHERE username = ?"));
        pstmt->setString(1, username);
        std::unique_ptr<sql::ResultSet> res(pstmt->executeQuery());

        // Check if the username exists
        if (res->next()) {
            int count = res->getInt(1);
            return count > 0; // Return true if count is greater than 0
        }

        // Clean up
        delete con;
    } catch (sql::SQLException& e) {
        std::cerr << "SQL Error: " << e.what() << std::endl;
    }

    // Clean up
    delete con;
    return false; // Return false if any error occurs or user doesn't exist
}

int main() {
    std::string username;
    std::cout << "Enter username to check: ";
    std::cin >> username;

    if (doesUserExist(username)) {
        std::cout << "Username exists." << std::endl;
    } else {
        std::cout << "Username does not exist." << std::endl;
    }

    return 0;
}
