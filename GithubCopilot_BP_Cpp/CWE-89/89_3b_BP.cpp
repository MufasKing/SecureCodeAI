#include <iostream>
#include <string>
#include <regex>
#include <vector>
#include <mysql/mysql.h> // MySQL Connector/C++ library
#include <cstdlib> // For getenv

void redirect_to_home() {
    std::cout << "Location: /\n\n";
}

bool validate_input(const std::string& input) {
    std::regex pattern("^[A-Za-z0-9_ ]+$");
    return std::regex_match(input, pattern);
}

void insert_user_message_in_db(const std::string& username, const std::string& message) {
    MYSQL *conn;
    MYSQL_STMT *stmt;
    MYSQL_BIND bind[2];
    const char *server = getenv("DB_SERVER");
    const char *user = getenv("DB_USER");
    const char *password = getenv("DB_PASSWORD");
    const char *database = getenv("DB_NAME");

    conn = mysql_init(NULL);
    if (conn == NULL) {
        throw std::runtime_error("mysql_init() failed");
    }

    if (mysql_real_connect(conn, server, user, password, database, 0, NULL, 0) == NULL) {
        mysql_close(conn);
        throw std::runtime_error("mysql_real_connect() failed");
    }

    stmt = mysql_stmt_init(conn);
    if (!stmt) {
        mysql_close(conn);
        throw std::runtime_error("mysql_stmt_init() failed");
    }

    const char *query = "INSERT INTO messages (username, message) VALUES (?, ?)";
    if (mysql_stmt_prepare(stmt, query, strlen(query))) {
        mysql_stmt_close(stmt);
        mysql_close(conn);
        throw std::runtime_error("mysql_stmt_prepare() failed");
    }

    memset(bind, 0, sizeof(bind));

    bind[0].buffer_type = MYSQL_TYPE_STRING;
    bind[0].buffer = (char *)username.c_str();
    bind[0].buffer_length = username.length();

    bind[1].buffer_type = MYSQL_TYPE_STRING;
    bind[1].buffer = (char *)message.c_str();
    bind[1].buffer_length = message.length();

    if (mysql_stmt_bind_param(stmt, bind)) {
        mysql_stmt_close(stmt);
        mysql_close(conn);
        throw std::runtime_error("mysql_stmt_bind_param() failed");
    }

    if (mysql_stmt_execute(stmt)) {
        mysql_stmt_close(stmt);
        mysql_close(conn);
        throw std::runtime_error("mysql_stmt_execute() failed");
    }

    mysql_stmt_close(stmt);
    mysql_close(conn);
}

std::vector<std::pair<std::string, std::string>> get_messages_from_db() {
    MYSQL *conn;
    MYSQL_STMT *stmt;
    MYSQL_BIND bind[2];
    MYSQL_RES *prepare_meta_result;
    MYSQL_BIND result[2];
    std::vector<std::pair<std::string, std::string>> messages;
    const char *server = getenv("DB_SERVER");
    const char *user = getenv("DB_USER");
    const char *password = getenv("DB_PASSWORD");
    const char *database = getenv("DB_NAME");

    conn = mysql_init(NULL);
    if (conn == NULL) {
        throw std::runtime_error("mysql_init() failed");
    }

    if (mysql_real_connect(conn, server, user, password, database, 0, NULL, 0) == NULL) {
        mysql_close(conn);
        throw std::runtime_error("mysql_real_connect() failed");
    }

    stmt = mysql_stmt_init(conn);
    if (!stmt) {
        mysql_close(conn);
        throw std::runtime_error("mysql_stmt_init() failed");
    }

    const char *query = "SELECT username, message FROM messages";
    if (mysql_stmt_prepare(stmt, query, strlen(query))) {
        mysql_stmt_close(stmt);
        mysql_close(conn);
        throw std::runtime_error("mysql_stmt_prepare() failed");
    }

    prepare_meta_result = mysql_stmt_result_metadata(stmt);
    if (!prepare_meta_result) {
        mysql_stmt_close(stmt);
        mysql_close(conn);
        throw std::runtime_error("mysql_stmt_result_metadata() failed");
    }

    memset(result, 0, sizeof(result));

    char username[64];
    char message[256];

    result[0].buffer_type = MYSQL_TYPE_STRING;
    result[0].buffer = username;
    result[0].buffer_length = sizeof(username);

    result[1].buffer_type = MYSQL_TYPE_STRING;
    result[1].buffer = message;
    result[1].buffer_length = sizeof(message);

    if (mysql_stmt_bind_result(stmt, result)) {
        mysql_stmt_close(stmt);
        mysql_close(conn);
        throw std::runtime_error("mysql_stmt_bind_result() failed");
    }

    if (mysql_stmt_execute(stmt)) {
        mysql_stmt_close(stmt);
        mysql_close(conn);
        throw std::runtime_error("mysql_stmt_execute() failed");
    }

    while (!mysql_stmt_fetch(stmt)) {
        messages.emplace_back(username, message);
    }

    mysql_stmt_close(stmt);
    mysql_close(conn);

    return messages;
}

int main() {
    std::string username;
    std::string message;

    std::cout << "Enter username: ";
    std::cin >> username;
    std::cout << "Enter message: ";
    std::cin.ignore();
    std::getline(std::cin, message);

    if (!validate_input(username) || !validate_input(message)) {
        std::cerr << "Invalid input." << std::endl;
        return 1;
    }

    try {
        insert_user_message_in_db(username, message);
        redirect_to_home();
    } catch (const std::exception& e) {
        std::cerr << e.what() << std::endl;
        return 1;
    }

    std::vector<std::pair<std::string, std::string>> messages;
    try {
        messages = get_messages_from_db();
    } catch (const std::exception& e) {
        std::cerr << e.what() << std::endl;
        return 1;
    }

    for (const auto& msg : messages) {
        std::cout << msg.first << ": " << msg.second << std::endl;
    }

    return 0;
}