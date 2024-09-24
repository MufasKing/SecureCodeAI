#include <iostream>
#include <string>

void do_login(const std::string& username, const std::string& password) {
    const std::string correct_username = "admin";
    const std::string correct_password = "password";

    if (username == correct_username && password == correct_password) {
        std::cout << "Content-Type: text/html\r\n";
        std::cout << "Set-Cookie: session_username=" << username << "\r\n";
        std::cout << "Location: /cgi-bin/secret.cgi\r\n\r\n";
        std::cout << "<html><head><title>Redirecting...</title></head><body>";
        std::cout << "<h1>Redirecting to secret page...</h1></body></html>";
    } else {
        std::cout << "Content-Type: text/html\r\n\r\n";
        std::cout << "<html><head><title>Login Failed</title></head><body>";
        std::cout << "<h1>Login Failed</h1>";
        std::cout << "<p>Invalid username or password. Please try again.</p>";
        std::cout << "<a href=\"/cgi-bin/login.cgi\">Back to Login</a>";
        std::cout << "</body></html>";
    }
}

int main() {
    std::cout << "Content-Type: text/html\r\n\r\n";

    std::string query_string = getenv("QUERY_STRING");
    std::string username, password;

    // Parse query string to get username and password
    if (query_string.find("username=") != std::string::npos && 
        query_string.find("password=") != std::string::npos) {
        size_t username_start = query_string.find("username=") + 9;
        size_t username_end = query_string.find("&", username_start);
        username = query_string.substr(username_start, username_end - username_start);

        size_t password_start = query_string.find("password=") + 9;
        password = query_string.substr(password_start);
    }

    do_login(username, password);
    return 0;
}
