#include <iostream>
#include <fstream>
#include <mysql/mysql.h>
#include <vector>
#include <stdexcept>

// Function to read database credentials from a configuration file
std::vector<std::string> read_db_credentials(const std::string& filepath) {
    std::ifstream file(filepath);
    std::vector<std::string> credentials;
    std::string line;
    while (std::getline(file, line)) {
        credentials.push_back(line);
    }
    return credentials;
}

// Function to validate the image file
bool validate_image_file(const std::string& filepath) {
    std::ifstream file(filepath, std::ios::binary);
    if (!file) {
        std::cerr << "File does not exist." << std::endl;
        return false;
    }
    // Additional validation can be added here (e.g., checking file headers)
    return true;
}

// Function to connect to the MySQL database
MYSQL* connect_to_db(const std::vector<std::string>& credentials) {
    MYSQL* conn = mysql_init(nullptr);
    if (conn == nullptr) {
        throw std::runtime_error("mysql_init() failed");
    }

    if (mysql_real_connect(conn, credentials[0].c_str(), credentials[1].c_str(),
                           credentials[2].c_str(), credentials[3].c_str(), 0, nullptr, 0) == nullptr) {
        std::string error_msg = "mysql_real_connect() failed: " + std::string(mysql_error(conn));
        mysql_close(conn);
        throw std::runtime_error(error_msg);
    }

    return conn;
}

// Function to store the image in the database
void store_image_in_db(MYSQL* conn, const std::string& filepath) {
    std::ifstream file(filepath, std::ios::binary);
    std::vector<char> buffer((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());

    const char* query = "INSERT INTO images (image_data) VALUES (?)";
    MYSQL_STMT* stmt = mysql_stmt_init(conn);
    if (!stmt) {
        throw std::runtime_error("mysql_stmt_init() failed");
    }

    if (mysql_stmt_prepare(stmt, query, strlen(query))) {
        std::string error_msg = "mysql_stmt_prepare() failed: " + std::string(mysql_stmt_error(stmt));
        mysql_stmt_close(stmt);
        throw std::runtime_error(error_msg);
    }

    MYSQL_BIND bind[1];
    memset(bind, 0, sizeof(bind));

    bind[0].buffer_type = MYSQL_TYPE_BLOB;
    bind[0].buffer = buffer.data();
    bind[0].buffer_length = buffer.size();

    if (mysql_stmt_bind_param(stmt, bind)) {
        std::string error_msg = "mysql_stmt_bind_param() failed: " + std::string(mysql_stmt_error(stmt));
        mysql_stmt_close(stmt);
        throw std::runtime_error(error_msg);
    }

    if (mysql_stmt_execute(stmt)) {
        std::string error_msg = "mysql_stmt_execute() failed: " + std::string(mysql_stmt_error(stmt));
        mysql_stmt_close(stmt);
        throw std::runtime_error(error_msg);
    }

    mysql_stmt_close(stmt);
}

int main() {
    try {
        std::string filepath;
        std::cout << "Enter the path to the image file: ";
        std::cin >> filepath;

        if (!validate_image_file(filepath)) {
            return 1;
        }

        std::vector<std::string> credentials = read_db_credentials("db_config.txt");
        MYSQL* conn = connect_to_db(credentials);

        store_image_in_db(conn, filepath);

        mysql_close(conn);
        std::cout << "Image stored successfully." << std::endl;
    } catch (const std::exception& ex) {
        std::cerr << "Error: " << ex.what() << std::endl;
        return 1;
    }

    return 0;
}