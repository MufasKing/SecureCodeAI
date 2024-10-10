#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <cppconn/driver.h>
#include <cppconn/exception.h>
#include <cppconn/resultset.h>
#include <cppconn/statement.h>
#include <cppconn/prepared_statement.h>
#include <openssl/bio.h>
#include <openssl/evp.h>
#include <openssl/buffer.h>

// Function to read file into a byte array
std::vector<unsigned char> readFile(const std::string& filePath) {
    std::ifstream file(filePath, std::ios::binary);
    std::vector<unsigned char> buffer((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
    return buffer;
}

// Function to convert byte array to base64 string
std::string base64Encode(const std::vector<unsigned char>& buffer) {
    BIO *bio, *b64;
    BUF_MEM *bufferPtr;
    b64 = BIO_new(BIO_f_base64());
    bio = BIO_new(BIO_s_mem());
    bio = BIO_push(b64, bio);
    BIO_write(bio, buffer.data(), buffer.size());
    BIO_flush(bio);
    BIO_get_mem_ptr(bio, &bufferPtr);
    std::string base64Str(bufferPtr->data, bufferPtr->length - 1);
    BIO_free_all(bio);
    return base64Str;
}

// Function to upload image
void upload_image(const std::string& imagePath, const std::string& imageName) {
    try {
        // Read image file
        std::vector<unsigned char> imageBuffer = readFile(imagePath);

        // Convert image to base64
        std::string base64Image = base64Encode(imageBuffer);

        // Database connection
        sql::Driver *driver;
        sql::Connection *con;
        sql::PreparedStatement *pstmt;

        driver = get_driver_instance();
        con = driver->connect("tcp://127.0.0.1:3306", "user", "password");
        con->setSchema("database_name");

        // Insert image name and base64 string into database
        pstmt = con->prepareStatement("INSERT INTO images (name, base64) VALUES (?, ?)");
        pstmt->setString(1, imageName);
        pstmt->setString(2, base64Image);
        pstmt->execute();

        delete pstmt;
        delete con;
    } catch (sql::SQLException &e) {
        std::cerr << "SQL error: " << e.what() << std::endl;
    } catch (std::exception &e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
}

int main() {
    // Example usage
    upload_image("path/to/image.jpg", "image.jpg");
    return 0;
}