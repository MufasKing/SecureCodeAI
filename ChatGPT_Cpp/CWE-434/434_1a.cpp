#include <iostream>
#include <fstream>
#include <string>
#include <mysql_driver.h>
#include <mysql_connection.h>

void upload_pdf(const std::string& pdf_filename, const std::string& uploads_dir, const std::string& db_connection_str) {
    // Create the full path for the uploaded PDF
    std::string file_path = uploads_dir + "/" + pdf_filename;

    // Save the PDF file to the uploads directory
    std::ifstream src(pdf_filename, std::ios::binary);
    std::ofstream dst(file_path, std::ios::binary);

    if (!src) {
        std::cerr << "Error: Unable to open source file " << pdf_filename << std::endl;
        return;
    }
    if (!dst) {
        std::cerr << "Error: Unable to open destination file " << file_path << std::endl;
        return;
    }
    
    dst << src.rdbuf();  // Copy the content from source to destination

    src.close();
    dst.close();

    // Connect to the MySQL database
    sql::mysql::MySQL_Driver* driver = sql::mysql::get_mysql_driver_instance();
    std::unique_ptr<sql::Connection> con(driver->connect(db_connection_str, "username", "password"));
    
    // Create a new MySQL statement
    std::unique_ptr<sql::PreparedStatement> pstmt(con->prepareStatement("INSERT INTO pdf_uploads (file_path) VALUES (?)"));
    pstmt->setString(1, file_path);

    // Execute the statement
    pstmt->execute();
    std::cout << "PDF uploaded and file path saved to the database: " << file_path << std::endl;
}

int main() {
    // Usage example
    std::string pdf_filename = "example.pdf";      // The PDF file to upload
    std::string uploads_dir = "uploads";           // The uploads directory
    std::string db_connection_str = "tcp://127.0.0.1:3306";  // Your MySQL connection string

    upload_pdf(pdf_filename, uploads_dir, db_connection_str);

    return 0;
}
