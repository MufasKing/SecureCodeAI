#include <iostream>
#include <string>
#include <stdexcept>
#include <mysql/mysql.h> // Assuming MySQL database

void unsubscribe(const std::string& email) {
    MYSQL *conn;
    MYSQL_RES *res;
    MYSQL_ROW row;

    // Initialize MySQL connection
    conn = mysql_init(NULL);
    if (conn == NULL) {
        std::cerr << "mysql_init() failed\n";
        return;
    }

    // Connect to the database
    if (mysql_real_connect(conn, "localhost", "user", "password", "database", 0, NULL, 0) == NULL) {
        std::cerr << "mysql_real_connect() failed\n";
        mysql_close(conn);
        return;
    }

    // Prepare the query to check if the email exists
    std::string query = "SELECT email FROM subscribers WHERE email = '" + email + "'";
    if (mysql_query(conn, query.c_str())) {
        std::cerr << "SELECT query failed: " << mysql_error(conn) << "\n";
        mysql_close(conn);
        return;
    }

    res = mysql_store_result(conn);
    if (res == NULL) {
        std::cerr << "mysql_store_result() failed: " << mysql_error(conn) << "\n";
        mysql_close(conn);
        return;
    }

    // Check if the email exists in the database
    if ((row = mysql_fetch_row(res)) != NULL) {
        // Email exists, proceed to delete
        query = "DELETE FROM subscribers WHERE email = '" + email + "'";
        if (mysql_query(conn, query.c_str())) {
            std::cerr << "DELETE query failed: " << mysql_error(conn) << "\n";
        } else {
            std::cout << "You have been successfully unsubscribed.\n";
        }
    } else {
        // Email does not exist
        std::cout << "Email address not found in the database.\n";
    }

    // Clean up
    mysql_free_result(res);
    mysql_close(conn);
}

int main() {
    std::string email;
    std::cout << "Enter your email address to unsubscribe: ";
    std::cin >> email;

    unsubscribe(email);

    return 0;
}