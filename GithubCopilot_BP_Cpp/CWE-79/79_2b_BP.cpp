#include <iostream>
#include <string>
#include <stdexcept>
#include <unordered_map>

// Mock environment and request classes for demonstration purposes
class Environment {
public:
    std::string get_template(const std::string& template_name) {
        // Securely fetch the template from storage
        if (template_name == "home") {
            return "<html><body>Hello, {{ name }}!</body></html>";
        }
        throw std::runtime_error("Template not found");
    }
};

class Request {
public:
    std::string get_parameter(const std::string& param_name) {
        // Simulate getting a parameter from the request
        if (param_name == "name") {
            return "User"; // Example user input
        }
        throw std::runtime_error("Parameter not found");
    }
};

// Function to sanitize user input
std::string sanitize_input(const std::string& input) {
    std::string sanitized = input;
    // Perform sanitization (e.g., escaping HTML characters)
    // For simplicity, we'll just replace '<' and '>' with their HTML entities
    size_t pos = 0;
    while ((pos = sanitized.find('<', pos)) != std::string::npos) {
        sanitized.replace(pos, 1, "&lt;");
        pos += 4;
    }
    pos = 0;
    while ((pos = sanitized.find('>', pos)) != std::string::npos) {
        sanitized.replace(pos, 1, "&gt;");
        pos += 4;
    }
    return sanitized;
}

// Function to render the template with the given parameters
std::string render_template(const std::string& tmpl, const std::unordered_map<std::string, std::string>& params) {
    std::string rendered = tmpl;
    for (const auto& param : params) {
        std::string placeholder = "{{ " + param.first + " }}";
        size_t pos = 0;
        while ((pos = rendered.find(placeholder, pos)) != std::string::npos) {
            rendered.replace(pos, placeholder.length(), param.second);
            pos += param.second.length();
        }
    }
    return rendered;
}

// Function to render response from environment
std::string render_response_from_env(Environment& env, Request& req) {
    try {
        std::string name = sanitize_input(req.get_parameter("name"));
        std::string tmpl = env.get_template("home");
        std::unordered_map<std::string, std::string> params = { {"name", name} };
        std::string rendered_template = render_template(tmpl, params);
        return rendered_template;
    } catch (const std::exception& e) {
        return "Error: " + std::string(e.what());
    }
}

// Home function
std::string home(Environment& env, Request& req) {
    return render_response_from_env(env, req);
}

// Main function for demonstration
int main() {
    Environment env;
    Request req;
    std::string response = home(env, req);
    std::cout << response << std::endl;
    return 0;
}