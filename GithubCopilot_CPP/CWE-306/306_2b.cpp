#include <iostream>
#include <string>
#include <unordered_map>
#include "httplib.h" // Hypothetical HTTP library

using namespace httplib;

// Mock database
std::unordered_map<std::string, std::string> user_db = {
    {"user1", "password1"},
    {"user2", "password2"}
};

// Function to handle GET request for login
void login(const Request& req, Response& res) {
    std::string form = R"(
        <html>
        <body>
            <form action="/do_login" method="post">
                Username: <input type="text" name="username"><br>
                Password: <input type="password" name="password"><br>
                <input type="submit" value="Login">
            </form>
        </body>
        </html>
    )";
    res.set_content(form, "text/html");
}

// Function to handle POST request for login
void do_login(const Request& req, Response& res) {
    auto username = req.get_param_value("username");
    auto password = req.get_param_value("password");

    if (user_db.find(username) != user_db.end() && user_db[username] == password) {
        res.set_redirect("/user_page");
    } else {
        res.set_content("Invalid username or password", "text/plain");
    }
}

int main() {
    Server svr;

    svr.Get("/login", login);
    svr.Post("/do_login", do_login);

    svr.listen("0.0.0.0", 8080);
}