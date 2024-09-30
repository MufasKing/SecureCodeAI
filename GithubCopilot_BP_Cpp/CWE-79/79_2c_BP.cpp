#include <iostream>
#include <string>
#include <unordered_map>
#include <stdexcept>

// Mock environment class
class Environment {
public:
    std::string get_template(const std::string& template_name) {
        // Simulate fetching a template from the environment
        if (template_name == "home") {
            return "<html><body>Hello, {{ name }}!</body></html>";
        } else {
            throw std::runtime_error("Template not found");
        }
    }
};

// Function to safely render a template with the provided context
std::string render_template(const std::string& tmpl, const std::unordered_map<std::string, std::string>& context) {
    std::string rendered = tmpl;
    for (const auto& pair : context) {
        std::string placeholder = "{{ " + pair.first + " }}";
        size_t pos = rendered.find(placeholder);
        if (pos != std::string::npos) {
            rendered.replace(pos, placeholder.length(), pair.second);
        }
    }
    return rendered;
}

// Function to render response from environment
std::string render_response_from_env(Environment& env, const std::unordered_map<std::string, std::string>& request) {
    try {
        // Input validation
        if (request.find("name") == request.end()) {
            throw std::invalid_argument("Missing 'name' parameter in request");
        }

        // Get the name parameter from the user request
        std::string name = request.at("name");

        // Get the template from the environment
        std::string tmpl = env.get_template("home");

        // Render the template with the name parameter from the request
        std::unordered_map<std::string, std::string> context = { {"name", name} };
        std::string rendered_template = render_template(tmpl, context);

        // Return a response with the rendered template
        return rendered_template;
    } catch (const std::exception& e) {
        // Error handling
        return std::string("Error: ") + e.what();
    }
}

// Home function
std::string home(Environment& env, const std::unordered_map<std::string, std::string>& request) {
    // Call the render_response_from_env function with the env variable
    std::string response = render_response_from_env(env, request);

    // Return the response from the render_response_from_env
    return response;
}

// Example usage
int main() {
    Environment env;
    std::unordered_map<std::string, std::string> request = { {"name", "John"} };
    std::string response = home(env, request);
    std::cout << response << std::endl;
    return 0;
}