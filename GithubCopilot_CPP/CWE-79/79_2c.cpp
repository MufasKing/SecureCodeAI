#include <string>
#include <map>

// Mock classes to simulate environment and request handling
class Environment {
public:
    std::string get_template(const std::string& template_name) {
        // Simulate getting a template from the environment
        return "Hello, {{ name }}!";
    }
};

class Request {
public:
    std::string get_parameter(const std::string& param_name) {
        // Simulate getting a parameter from the user request
        return "World";
    }
};

class Response {
public:
    std::string content;
    Response(const std::string& rendered_template) : content(rendered_template) {}
};

// Function to render response from environment
Response render_response_from_env(Environment& env, Request& request) {
    std::string name = request.get_parameter("name");
    std::string template_str = env.get_template("template_name");
    
    // Simulate rendering the template with the name parameter
    std::string rendered_template = template_str;
    size_t pos = rendered_template.find("{{ name }}");
    if (pos != std::string::npos) {
        rendered_template.replace(pos, 9, name);
    }
    
    return Response(rendered_template);
}

// Home function
Response home(Environment& env, Request& request) {
    return render_response_from_env(env, request);
}

// Example usage
int main() {
    Environment env;
    Request request;
    Response response = home(env, request);
    std::cout << response.content << std::endl;
    return 0;
}