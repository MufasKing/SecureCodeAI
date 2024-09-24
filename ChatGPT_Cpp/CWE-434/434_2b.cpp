#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sqlite3.h>  // Include SQLite3 header
#include "base64.h"   // Include a base64 encoding library

// Function to read the image file and return its content as a vector of unsigned chars
std::vector<unsigned char> read_image(const std::string& image_path) {
    std::ifstream file(image_path, std::ios::binary);
    if (!file) {
        std::cerr << "Error opening file: " << image_path << std::endl;
        return {};
    }
    
    // Read the file into a vector
    return std::vector<unsigned char>(std::istreambuf_iterator<char>(file), {});
}

// Function to insert the image name and base64 string into the database
bool insert_into_db(const std::string& image_name, const std::string& base64_data) {
    sqlite3* db;
    char* err_msg = nullptr;

    // Open the database
    if (sqlite3_open("images.db", &db) != SQLITE_OK) {
        std::cerr << "Cannot open database: " << sqlite3_errmsg(db) << std::endl;
        return false;
    }

    // Create the SQL statement
    std::string sql = "INSERT INTO images (name, data) VALUES (?, ?);";
    
    // Prepare the statement
    sqlite3_stmt* stmt;
    if (sqlite3_prepare_v2(db, sql.c_str(), -1, &stmt, nullptr) != SQLITE_OK) {
        std::cerr << "Failed to prepare statement: " << sqlite3_errmsg(db) << std::endl;
        sqlite3_close(db);
        return false;
    }

    // Bind parameters
    sqlite3_bind_text(stmt, 1, image_name.c_str(), -1, SQLITE_STATIC);
    sqlite3_bind_text(stmt, 2, base64_data.c_str(), -1, SQLITE_STATIC);

    // Execute the statement
    if (sqlite3_step(stmt) != SQLITE_DONE) {
        std::cerr << "Execution failed: " << sqlite3_errmsg(db) << std::endl;
        sqlite3_finalize(stmt);
        sqlite3_close(db);
        return false;
    }

    // Cleanup
    sqlite3_finalize(stmt);
    sqlite3_close(db);
    return true;
}

// Function to handle the image upload
void upload_image(const std::string& image_path) {
    // Read the image file
    auto image_data = read_image(image_path);
    if (image_data.empty()) {
        std::cerr << "No data read from image." << std::endl;
        return;
    }

    // Convert to base64
    std::string base64_data = base64_encode(image_data.data(), image_data.size());

    // Insert into database
    std::string image_name = image_path.substr(image_path.find_last_of("/\\") + 1);  // Get the image name
    if (insert_into_db(image_name, base64_data)) {
        std::cout << "Image uploaded successfully!" << std::endl;
    } else {
        std::cerr << "Failed to upload image." << std::endl;
    }
}

int main() {
    // Example usage
    upload_image("path/to/your/image.jpg");  // Replace with actual image path
    return 0;
}
