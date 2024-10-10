#include <iostream>
#include <string>
#include <mysql/mysql.h>
#include <openssl/md5.h>

using namespace std;

// Function to hash a password using MD5
string md5(const string& password) {
    unsigned char digest[MD5_DIGEST_LENGTH];
    MD5((unsigned char*)password.c_str(), password.size(), (unsigned char*)&digest);    

    char mdString[33];
    for(int i = 0; i < 16; i++)
        sprintf(&mdString[i*2], "%02x", (unsigned int)digest[i]);

    return string(mdString);
}

int main() {
    // Database connection variables
    MYSQL *conn;
    MYSQL_RES *res;
    MYSQL_ROW row;

    const char *server = "localhost";
    const char *user = "root";
    const char *password = "root"; // Set your database password
    const char *database = "testdb";

    // Initialize MySQL connection
    conn = mysql_init(NULL);

    // Connect to database
    if (!mysql_real_connect(conn, server, user, password, database, 0, NULL, 0)) {
        cerr << "MySQL connection failed: " << mysql_error(conn) << endl;
        return 1;
    }

    // Get username and password from user
    string username, user_password;
    cout << "Enter username: ";
    cin >> username;
    cout << "Enter password: ";
    cin >> user_password;

    // Hash the password
    string hashed_password = md5(user_password);

    // Create SQL query
    string query = "INSERT INTO users (username, password) VALUES ('" + username + "', '" + hashed_password + "')";

    // Execute SQL query
    if (mysql_query(conn, query.c_str())) {
        cerr << "MySQL query failed: " << mysql_error(conn) << endl;
        return 1;
    }

    cout << "User registered successfully!" << endl;

    // Close MySQL connection
    mysql_close(conn);

    return 0;
}