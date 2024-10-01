#include <iostream>
#include <string>
#include <stdexcept>
#include <mysql/mysql.h> // MySQL C API
#include <regex>
#include <mutex>

std::mutex db_mutex;

bool validate_email(const std::string& email) {
    const std::regex pattern(R"((\w+)(\.{1}\w+)*@(\w+)(\.\w+)+)");
    return std::regex_match(email, pattern);
}

MYSQL* connect_db() {
    const char *server = "localhost";
    const char *user = "db_user";
    const char *password = "db_password";
    const char *database = "mailing_list_db";

    MYSQL *conn = mysql_init(NULL);
    if (conn == NULL) {
        throw std::runtime_error("mysql_init() failed");
    }

    if (mysql_real_connect(conn, server, user, password, database, 0, NULL, 0) == NULL) {
        mysql_close(conn);
        throw std::runtime_error("mysql_real_connect() failed");
    }

    return conn;
}

bool is_email_in_db(MYSQL *conn, const std::string& email) {
    const char *query = "SELECT COUNT(*) FROM subscribers WHERE email = ?";
    MYSQL_STMT *stmt = mysql_stmt_init(conn);
    if (!stmt) {
        throw std::runtime_error("mysql_stmt_init() failed");
    }

    if (mysql_stmt_prepare(stmt, query, strlen(query))) {
        mysql_stmt_close(stmt);
        throw std::runtime_error("mysql_stmt_prepare() failed");
    }

    MYSQL_BIND bind[1];
    memset(bind, 0, sizeof(bind));
    bind[0].buffer_type = MYSQL_TYPE_STRING;
    bind[0].buffer = (char *)email.c_str();
    bind[0].buffer_length = email.length();

    if (mysql_stmt_bind_param(stmt, bind)) {
        mysql_stmt_close(stmt);
        throw std::runtime_error("mysql_stmt_bind_param() failed");
    }

    if (mysql_stmt_execute(stmt)) {
        mysql_stmt_close(stmt);
        throw std::runtime_error("mysql_stmt_execute() failed");
    }

    MYSQL_BIND result_bind[1];
    int count;
    memset(result_bind, 0, sizeof(result_bind));
    result_bind[0].buffer_type = MYSQL_TYPE_LONG;
    result_bind[0].buffer = (char *)&count;
    result_bind[0].buffer_length = sizeof(count);

    if (mysql_stmt_bind_result(stmt, result_bind)) {
        mysql_stmt_close(stmt);
        throw std::runtime_error("mysql_stmt_bind_result() failed");
    }

    if (mysql_stmt_fetch(stmt)) {
        mysql_stmt_close(stmt);
        throw std::runtime_error("mysql_stmt_fetch() failed");
    }

    mysql_stmt_close(stmt);
    return count > 0;
}

void unsubscribe_email(MYSQL *conn, const std::string& email) {
    const char *query = "DELETE FROM subscribers WHERE email = ?";
    MYSQL_STMT *stmt = mysql_stmt_init(conn);
    if (!stmt) {
        throw std::runtime_error("mysql_stmt_init() failed");
    }

    if (mysql_stmt_prepare(stmt, query, strlen(query))) {
        mysql_stmt_close(stmt);
        throw std::runtime_error("mysql_stmt_prepare() failed");
    }

    MYSQL_BIND bind[1];
    memset(bind, 0, sizeof(bind));
    bind[0].buffer_type = MYSQL_TYPE_STRING;
    bind[0].buffer = (char *)email.c_str();
    bind[0].buffer_length = email.length();

    if (mysql_stmt_bind_param(stmt, bind)) {
        mysql_stmt_close(stmt);
        throw std::runtime_error("mysql_stmt_bind_param() failed");
    }

    if (mysql_stmt_execute(stmt)) {
        mysql_stmt_close(stmt);
        throw std::runtime_error("mysql_stmt_execute() failed");
    }

    mysql_stmt_close(stmt);
}

int main() {
    std::string email;
    std::cout << "Enter email to unsubscribe: ";
    std::cin >> email;

    if (!validate_email(email)) {
        std::cerr << "Invalid email format." << std::endl;
        return 1;
    }

    try {
        std::lock_guard<std::mutex> lock(db_mutex);
        MYSQL *conn = connect_db();

        if (is_email_in_db(conn, email)) {
            unsubscribe_email(conn, email);
            std::cout << "You have been unsubscribed." << std::endl;
        } else {
            std::cout << "Email not found in the database." << std::endl;
        }

        mysql_close(conn);
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}