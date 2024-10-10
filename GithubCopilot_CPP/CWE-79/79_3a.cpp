#include "crow.h"
#include <fstream>
#include <sstream>

// Function to read the template file and replace the placeholder with the username
std::string render_template(const std::string& username) {
    std::ifstream file("hello.html");
    std::stringstream buffer;
    buffer << file.rdbuf();
    std::string content = buffer.str();

    // Replace placeholder with username
    size_t pos = content.find("{{username}}");
    if (pos != std::string::npos) {
        content.replace(pos, 11, username);
    }

    return content;
}

// Function to handle the /hello/<username> route
crow::response hello(const crow::request& req, const std::string& username) {
    std::string rendered_content = render_template(username);
    return crow::response(rendered_content);
}

int main() {
    crow::SimpleApp app;

    // Define the route
    CROW_ROUTE(app, "/hello/<string>")
    ([](const crow::request& req, const std::string& username){
        return hello(req, username);
    });

    // Start the server
    app.port(18080).multithreaded().run();
}