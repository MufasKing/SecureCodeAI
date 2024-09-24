#include <iostream>
#include <fstream>
#include <mysql/mysql.h>
#include <string>

// Function to upload PDF
void upload_pdf(const std::string& pdf_file_name) {
    // Define the uploads folder path
    std::string uploads_folder = "uploads/";
    std::string file_path = uploads_folder + pdf_file_name;

    // Save the PDF file to the uploads folder
    std::ifstream src(pdf_file_name, std::ios::binary);
    std::ofstream dst(file_path, std::ios::binary);
    dst << src.rdbuf();
    src.close();
    dst.close();

    // MySQL connection details
    const char* server = "localhost";
    const char* user = "root";
    const char* password = "password"; // Update with your MySQL password
    const char* database = "your_database"; // Update with your database name

    // Initialize MySQL connection
    MYSQL* conn;
    conn = mysql_init(NULL);

    // Connect to the database
    if (!mysql_real_connect(conn, server, user, password, database, 0, NULL, 0)) {
        std::cerr << "MySQL connection failed: " << mysql_error(conn) << std::endl;
        return;
    }

    // Insert file path into the database
    std::string query = "INSERT INTO pdf_files (file_path) VALUES ('" + file_path + "')";
    if (mysql_query(conn, query.c_str())) {
        std::cerr << "INSERT failed: " << mysql_error(conn) << std::endl;
        mysql_close(conn);
        return;
    }

    // Close the MySQL connection
    mysql_close(conn);

    std::cout << "PDF file uploaded and file path saved to database successfully." << std::endl;
}

// Function to download PDF using file path from database
void download_pdf(const std::string& pdf_file_name) {
    std::string uploads_folder = "uploads/";
    std::string file_path = uploads_folder + pdf_file_name;

    // Check if file exists
    std::ifstream file(file_path);
    if (!file) {
        std::cerr << "File not found: " << file_path << std::endl;
        return;
    }

    // Simulate file download
    std::cout << "Downloading file: " << file_path << std::endl;
    // Here you can add code to handle the actual file download process
}

int main() {
    // Example usage
    upload_pdf("example.pdf");
    download_pdf("example.pdf");

    return 0;
}