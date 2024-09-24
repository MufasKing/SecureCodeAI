#include <iostream>
#include <fstream>
#include <vector>
#include <mysql_driver.h>
#include <mysql_connection.h>

using namespace std;
using namespace mysql;

void storeImageInDatabase(const string &imagePath, const string &dbName, const string &tableName) {
    // Load the image file into a vector
    ifstream imageFile(imagePath, ios::binary);
    if (!imageFile) {
        cerr << "Could not open the file: " << imagePath << endl;
        return;
    }

    vector<char> imageBuffer((istreambuf_iterator<char>(imageFile)), {});
    imageFile.close();

    // Establish a connection to the MySQL database
    sql::mysql::MySQL_Driver *driver = sql::mysql::get_mysql_driver_instance();
    unique_ptr<sql::Connection> con(driver->connect("tcp://127.0.0.1:3306", "username", "password"));

    // Select the database
    con->setSchema(dbName);

    // Create a prepared statement to insert the image
    unique_ptr<sql::PreparedStatement> pstmt(con->prepareStatement("INSERT INTO " + tableName + " (image) VALUES (?)"));
    
    pstmt->setBlob(1, imageBuffer.data(), imageBuffer.size());

    // Execute the statement
    pstmt->executeUpdate();

    cout << "Image stored successfully in database." << endl;
}

int main() {
    string imagePath;
    string dbName = "your_database_name"; // Replace with your database name
    string tableName = "your_table_name"; // Replace with your table name

    cout << "Enter the path of the image file: ";
    cin >> imagePath;

    storeImageInDatabase(imagePath, dbName, tableName);

    return 0;
}
