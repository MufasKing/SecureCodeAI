#include <string>
#include <map>

// Mock classes to simulate environment and request handling
class Request {
public:
    std::string get_param(const std::string& key) const {
        // Simulate getting a parameter from the request
        if (key == "name") {
            return "John Doe";
        }
        return "";
    }
};

class Environment {
public:
    std::string get_template() const {
        // Simulate getting a template from the environment
        return "Hello, {{name}}!";
    }
};

class Response {
public:
    std::string content;
    Response(const std::string& rendered_template) : content(rendered_template) {}
};

// Function to render the response from the environment
Response render_response_from_env(const Environment& env, const Request& request) {
    std::string name = request.get_param("name");
    std::string template_str = env.get_template();
    
    // Simulate rendering the template with the name parameter
    std::string rendered_template = template_str;
    size_t pos = rendered_template.find("{{name}}");
    if (pos != std::string::npos) {
        rendered_template.replace(pos, 8, name);
    }
    
    return Response(rendered_template);
}

// Home function
Response home(const Environment& env, const Request& request) {
    return render_response_from_env(env, request);
}

// Example usage
int main() {
    Environment env;
    Request request;
    Response response = home(env, request);
    // Output the response content
    std::cout << response.content << std::endl;
    return 0;
}