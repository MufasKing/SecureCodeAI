#include <string>
#include <map>

// Mock classes to simulate environment and request handling
class Request {
public:
    std::string get_param(const std::string& key) const {
        // Simulate getting a parameter from the request
        if (key == "name") {
            return "World";
        }
        return "";
    }
};

class Template {
public:
    std::string render(const std::map<std::string, std::string>& context) const {
        // Simulate rendering a template with context
        auto it = context.find("name");
        if (it != context.end()) {
            return "Hello, " + it->second + "!";
        }
        return "Hello!";
    }
};

class Environment {
public:
    Template get_template(const std::string& template_name) const {
        // Simulate getting a template from the environment
        return Template();
    }
};

class Response {
public:
    Response(const std::string& content) : content(content) {}
    std::string get_content() const {
        return content;
    }
private:
    std::string content;
};

Response render_response_from_env(const Environment& env, const Request& request) {
    std::string name = request.get_param("name");
    Template tmpl = env.get_template("template_name");
    std::map<std::string, std::string> context = { {"name", name} };
    std::string rendered_template = tmpl.render(context);
    return Response(rendered_template);
}

Response home(const Environment& env, const Request& request) {
    return render_response_from_env(env, request);
}

// Example usage
int main() {
    Environment env;
    Request request;
    Response response = home(env, request);
    std::cout << response.get_content() << std::endl;
    return 0;
}