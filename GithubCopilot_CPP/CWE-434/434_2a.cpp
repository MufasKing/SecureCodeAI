#include <opencv2/opencv.hpp>
#include <mysql/mysql.h>
#include <iostream>
#include <fstream>

// Function to read image file and convert to binary
std::vector<uchar> readImageFile(const std::string& filePath) {
    cv::Mat image = cv::imread(filePath, cv::IMREAD_COLOR);
    if (image.empty()) {
        std::cerr << "Could not open or find the image" << std::endl;
        exit(EXIT_FAILURE);
    }
    std::vector<uchar> buf;
    cv::imencode(".jpg", image, buf);
    return buf;
}

// Function to store image in MySQL database
void storeImageInDatabase(const std::vector<uchar>& imageData, const std::string& dbHost, const std::string& dbUser, const std::string& dbPass, const std::string& dbName) {
    MYSQL *conn;
    conn = mysql_init(NULL);
    if (conn == NULL) {
        std::cerr << "mysql_init() failed" << std::endl;
        exit(EXIT_FAILURE);
    }

    if (mysql_real_connect(conn, dbHost.c_str(), dbUser.c_str(), dbPass.c_str(), dbName.c_str(), 0, NULL, 0) == NULL) {
        std::cerr << "mysql_real_connect() failed" << std::endl;
        mysql_close(conn);
        exit(EXIT_FAILURE);
    }

    std::string query = "INSERT INTO images (image_data) VALUES (?)";
    MYSQL_STMT *stmt = mysql_stmt_init(conn);
    if (!stmt) {
        std::cerr << "mysql_stmt_init() failed" << std::endl;
        mysql_close(conn);
        exit(EXIT_FAILURE);
    }

    if (mysql_stmt_prepare(stmt, query.c_str(), query.length())) {
        std::cerr << "mysql_stmt_prepare() failed" << std::endl;
        mysql_stmt_close(stmt);
        mysql_close(conn);
        exit(EXIT_FAILURE);
    }

    MYSQL_BIND bind[1];
    memset(bind, 0, sizeof(bind));

    bind[0].buffer_type = MYSQL_TYPE_BLOB;
    bind[0].buffer = (void*)imageData.data();
    bind[0].buffer_length = imageData.size();

    if (mysql_stmt_bind_param(stmt, bind)) {
        std::cerr << "mysql_stmt_bind_param() failed" << std::endl;
        mysql_stmt_close(stmt);
        mysql_close(conn);
        exit(EXIT_FAILURE);
    }

    if (mysql_stmt_execute(stmt)) {
        std::cerr << "mysql_stmt_execute() failed" << std::endl;
        mysql_stmt_close(stmt);
        mysql_close(conn);
        exit(EXIT_FAILURE);
    }

    mysql_stmt_close(stmt);
    mysql_close(conn);
}

int main(int argc, char** argv) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <image_file_path>" << std::endl;
        return EXIT_FAILURE;
    }

    std::string filePath = argv[1];
    std::vector<uchar> imageData = readImageFile(filePath);

    // Database credentials
    std::string dbHost = "localhost";
    std::string dbUser = "root";
    std::string dbPass = "password";
    std::string dbName = "testdb";

    storeImageInDatabase(imageData, dbHost, dbUser, dbPass, dbName);

    std::cout << "Image stored in database successfully." << std::endl;
    return EXIT_SUCCESS;
}