#include <iostream>
#include <string>
#include <mysql/mysql.h> // Assuming MySQL database

bool checkUsernameExists(const std::string& username) {
    MYSQL *conn;
    MYSQL_RES *res;
    MYSQL_ROW row;

    const char *server = "localhost";
    const char *user = "root";
    const char *password = "password"; // Set your database password
    const char *database = "your_database"; // Set your database name

    conn = mysql_init(NULL);

    // Connect to database
    if (!mysql_real_connect(conn, server, user, password, database, 0, NULL, 0)) {
        std::cerr << "mysql_real_connect() failed\n";
        return false;
    }

    // Create query
    std::string query = "SELECT 1 FROM users WHERE username = '" + username + "' LIMIT 1";

    // Execute query
    if (mysql_query(conn, query.c_str())) {
        std::cerr << "SELECT query failed. Error: " << mysql_error(conn) << "\n";
        mysql_close(conn);
        return false;
    }

    res = mysql_store_result(conn);
    bool exists = (mysql_num_rows(res) > 0);

    // Clean up
    mysql_free_result(res);
    mysql_close(conn);

    return exists;
}

int main() {
    std::string username = "test_user";
    if (checkUsernameExists(username)) {
        std::cout << "Username exists.\n";
    } else {
        std::cout << "Username does not exist.\n";
    }
    return 0;
}