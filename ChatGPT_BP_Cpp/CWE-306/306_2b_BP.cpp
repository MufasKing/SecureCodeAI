#include <iostream>
#include <unordered_map>
#include <httplib.h>
#include <bcrypt.h>
#include <nlohmann/json.hpp>

// Simulating a database for simplicity
std::unordered_map<std::string, std::string> user_db = {
    {"user1", bcrypt::generateHash("SecurePass123")},
    {"user2", bcrypt::generateHash("AnotherPass456")}
};

// Simulating session management
std::unordered_map<std::string, std::string> session_db;

// Function to generate a simple HTML form for login
std::string login_form() {
    return R"(
    <html>
        <body>
            <h2>Login Form</h2>
            <form method="POST" action="/do_login">
                Username: <input type="text" name="username"><br>
                Password: <input type="password" name="password"><br>
                <input type="submit" value="Login">
            </form>
        </body>
    </html>
    )";
}

// Function to validate input (basic sanitization)
bool validate_input(const std::string& username, const std::string& password) {
    return !username.empty() && !password.empty() && username.size() <= 50 && password.size() <= 50;
}

// Function to generate a random session token (simple simulation)
std::string generate_session_token() {
    return "session_token_" + std::to_string(rand() % 100000);
}

// Error logging (simple console-based logging)
void log_error(const std::string& error_message) {
    std::cerr << "[ERROR] " << error_message << std::endl;
}

// Login page handler (GET request)
void login_page(const httplib::Request& req, httplib::Response& res) {
    res.set_content(login_form(), "text/html");
}

// Login processing (POST request)
void do_login(const httplib::Request& req, httplib::Response& res) {
    if (req.has_param("username") && req.has_param("password")) {
        std::string username = req.get_param_value("username");
        std::string password = req.get_param_value("password");

        // Input validation and sanitization
        if (!validate_input(username, password)) {
            log_error("Invalid input data");
            res.set_content("Invalid input. Please try again.", "text/plain");
            return;
        }

        // Check if user exists in the database
        if (user_db.find(username) != user_db.end()) {
            std::string stored_hash = user_db[username];

            // Check if the password matches using bcrypt
            if (bcrypt::validatePassword(password, stored_hash)) {
                std::string session_token = generate_session_token();
                session_db[session_token] = username;

                // Redirect to the user page
                res.set_redirect("/user_page?session=" + session_token);
            } else {
                log_error("Incorrect password attempt for user: " + username);
                res.set_content("Invalid username or password.", "text/plain");
            }
        } else {
            log_error("User not found: " + username);
            res.set_content("Invalid username or password.", "text/plain");
        }
    } else {
        log_error("Username or password not provided");
        res.set_content("Username and password are required.", "text/plain");
    }
}

// Simulated user page
void user_page(const httplib::Request& req, httplib::Response& res) {
    if (req.has_param("session")) {
        std::string session_token = req.get_param_value("session");

        // Check if session is valid
        if (session_db.find(session_token) != session_db.end()) {
            std::string username = session_db[session_token];
            res.set_content("Welcome, " + username + "!", "text/plain");
        } else {
            res.set_content("Invalid session. Please login again.", "text/plain");
        }
    } else {
        res.set_content("Session not found. Please login.", "text/plain");
    }
}

int main() {
    httplib::Server server;

    // GET request to serve login page
    server.Get("/login", login_page);

    // POST request to handle login
    server.Post("/do_login", do_login);

    // Simulated user page after successful login
    server.Get("/user_page", user_page);

    std::cout << "Server starting at http://localhost:8080\n";
    server.listen("localhost", 8080);

    return 0;
}
