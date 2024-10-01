#include <iostream>
#include <regex>
#include <string>
#include <curl/curl.h>
#include <mysql/mysql.h>

// Function to validate email format
bool isValidEmail(const std::string& email) {
    const std::regex pattern(R"((\w+)(\.{1}\w+)*@(\w+)(\.\w+)+)");
    return std::regex_match(email, pattern);
}

// Function to URL encode the email
std::string urlEncode(const std::string& value) {
    CURL* curl = curl_easy_init();
    char* output = curl_easy_escape(curl, value.c_str(), value.length());
    std::string encoded(output);
    curl_free(output);
    curl_easy_cleanup(curl);
    return encoded;
}

// Function to check if email exists in the database
bool emailExists(MYSQL* conn, const std::string& email) {
    const char* query = "SELECT COUNT(*) FROM users WHERE email = ?";
    MYSQL_STMT* stmt = mysql_stmt_init(conn);
    mysql_stmt_prepare(stmt, query, strlen(query));
    MYSQL_BIND bind[1];
    memset(bind, 0, sizeof(bind));
    bind[0].buffer_type = MYSQL_TYPE_STRING;
    bind[0].buffer = (char*)email.c_str();
    bind[0].buffer_length = email.length();
    mysql_stmt_bind_param(stmt, bind);
    mysql_stmt_execute(stmt);
    MYSQL_BIND result[1];
    memset(result, 0, sizeof(result));
    int count;
    result[0].buffer_type = MYSQL_TYPE_LONG;
    result[0].buffer = &count;
    mysql_stmt_bind_result(stmt, result);
    mysql_stmt_fetch(stmt);
    mysql_stmt_close(stmt);
    return count > 0;
}

// Function to call PHP script to unsubscribe email
int callPhpScript(const std::string& email) {
    CURL* curl;
    CURLcode res;
    curl = curl_easy_init();
    if(curl) {
        std::string url = "https://example.com/unsubscribe.php?email=" + urlEncode(email);
        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
        curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);
        res = curl_easy_perform(curl);
        long response_code;
        curl_easy_getinfo(curl, CURLINFO_RESPONSE_CODE, &response_code);
        curl_easy_cleanup(curl);
        if(res != CURLE_OK || response_code != 200) {
            return 0;
        }
        return 1;
    }
    return 0;
}

int main() {
    std::string email;
    std::cout << "Enter email: ";
    std::cin >> email;

    if (!isValidEmail(email)) {
        std::cerr << "Invalid email format." << std::endl;
        return 0;
    }

    MYSQL* conn;
    conn = mysql_init(NULL);
    if (conn == NULL) {
        std::cerr << "mysql_init() failed." << std::endl;
        return 0;
    }

    if (mysql_real_connect(conn, "localhost", "user", "password", "database", 0, NULL, 0) == NULL) {
        std::cerr << "mysql_real_connect() failed." << std::endl;
        mysql_close(conn);
        return 0;
    }

    if (!emailExists(conn, email)) {
        mysql_close(conn);
        return 0;
    }

    int result = callPhpScript(email);
    mysql_close(conn);
    return result;
}