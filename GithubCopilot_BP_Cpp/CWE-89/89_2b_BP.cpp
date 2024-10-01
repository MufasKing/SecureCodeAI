#include <iostream>
#include <string>
#include <stdexcept>
#include <mysql/mysql.h> // MySQL C API

void redirectToProfile() {
    std::cout << "Redirecting to profile page..." << std::endl;
    // Implementation for redirection (platform-specific)
}

bool isValidStockName(const std::string& stock_name) {
    // Add validation logic for stock name
    return !stock_name.empty();
}

bool isValidQuantity(int quantity) {
    // Add validation logic for quantity
    return quantity > 0;
}

int main() {
    std::string username = "user123"; // Example username
    std::string stock_name;
    int stock_quantity;

    std::cout << "Enter stock name: ";
    std::getline(std::cin, stock_name);
    std::cout << "Enter stock quantity: ";
    std::cin >> stock_quantity;

    if (!isValidStockName(stock_name) || !isValidQuantity(stock_quantity)) {
        std::cerr << "Invalid input." << std::endl;
        return 1;
    }

    MYSQL *conn;
    MYSQL_STMT *stmt;
    MYSQL_BIND bind[3];
    const char *server = "localhost";
    const char *user = "db_user";
    const char *password = "db_password";
    const char *database = "stock_db";

    conn = mysql_init(NULL);
    if (conn == NULL) {
        std::cerr << "mysql_init() failed" << std::endl;
        return 1;
    }

    if (mysql_real_connect(conn, server, user, password, database, 0, NULL, 0) == NULL) {
        std::cerr << "mysql_real_connect() failed" << std::endl;
        mysql_close(conn);
        return 1;
    }

    const char *query = "INSERT INTO buy_orders (username, stock_name, stock_quantity) VALUES (?, ?, ?)";
    stmt = mysql_stmt_init(conn);
    if (!stmt) {
        std::cerr << "mysql_stmt_init() failed" << std::endl;
        mysql_close(conn);
        return 1;
    }

    if (mysql_stmt_prepare(stmt, query, strlen(query))) {
        std::cerr << "mysql_stmt_prepare() failed" << std::endl;
        mysql_stmt_close(stmt);
        mysql_close(conn);
        return 1;
    }

    memset(bind, 0, sizeof(bind));

    bind[0].buffer_type = MYSQL_TYPE_STRING;
    bind[0].buffer = (char *)username.c_str();
    bind[0].buffer_length = username.length();

    bind[1].buffer_type = MYSQL_TYPE_STRING;
    bind[1].buffer = (char *)stock_name.c_str();
    bind[1].buffer_length = stock_name.length();

    bind[2].buffer_type = MYSQL_TYPE_LONG;
    bind[2].buffer = (char *)&stock_quantity;
    bind[2].buffer_length = sizeof(stock_quantity);

    if (mysql_stmt_bind_param(stmt, bind)) {
        std::cerr << "mysql_stmt_bind_param() failed" << std::endl;
        mysql_stmt_close(stmt);
        mysql_close(conn);
        return 1;
    }

    if (mysql_stmt_execute(stmt)) {
        std::cerr << "mysql_stmt_execute() failed" << std::endl;
        mysql_stmt_close(stmt);
        mysql_close(conn);
        return 1;
    }

    mysql_stmt_close(stmt);
    mysql_close(conn);

    redirectToProfile();
    return 0;
}