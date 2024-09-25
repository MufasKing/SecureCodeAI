#include "crow_all.h"
#include <fstream>
#include <sstream>
#include <string>

// Function to read the content of the template file
std::string readTemplate(const std::string& filename) {
    std::ifstream file(filename);
    if (!file.is_open()) {
        return "Template not found!";
    }
    std::ostringstream buffer;
    buffer << file.rdbuf();
    return buffer.str();
}

// Function to render the template with the username
std::string renderTemplate(const std::string& username) {
    std::string templateContent = readTemplate("hello.html");
    // Replace the placeholder in the template with the actual username
    std::string renderedContent = templateContent;
    size_t pos = renderedContent.find("{{ username }}");
    if (pos != std::string::npos) {
        renderedContent.replace(pos, 14, username); // 14 is the length of "{{ username }}"
    }
    return renderedContent;
}

int main() {
    crow::SimpleApp app;

    // Route for /hello/<username>
    CROW_ROUTE(app, "/hello/<string>")([&](const crow::request& req, const std::string& username) {
        // Render the template and return the response
        std::string response = renderTemplate(username);
        return crow::response(response);
    });

    app.port(18080).multithreaded().run();
}
