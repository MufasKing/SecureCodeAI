#include <iostream>
#include <unordered_map>
#include <functional>
#include <string>

// Function to escape special characters for HTML
std::string escape(const std::string& input) {
    std::string output;
    for (char c : input) {
        switch (c) {
            case '&': output += "&amp;"; break;
            case '<': output += "&lt;"; break;
            case '>': output += "&gt;"; break;
            case '"': output += "&quot;"; break;
            case '\'': output += "&#39;"; break;
            default: output += c; break;
        }
    }
    return output;
}

// Class to handle URL mapping and function decoration
class Router {
public:
    using Handler = std::function<std::string(const std::string&)>;

    // Decorator to register a URL with a handler function
    void add_route(const std::string& url, Handler handler) {
        routes[url] = handler;
    }

    // Function to handle requests
    std::string handle_request(const std::string& url, const std::string& username) {
        auto it = routes.find(url);
        if (it != routes.end()) {
            return it->second(username);
        }
        return "404 Not Found";
    }

private:
    std::unordered_map<std::string, Handler> routes;
};

// Function to return greeting message
std::string hello(const std::string& username) {
    return "Hello " + escape(username);
}

int main() {
    Router router;

    // Registering the URL /hello/username with the hello function
    router.add_route("/hello/", hello);

    // Simulate a request
    std::string url = "/hello/";
    std::string username = "Alice & Bob";  // Example username with special character

    std::string response = router.handle_request(url, username);
    std::cout << response << std::endl;  // Output: Hello Alice &amp; Bob

    return 0;
}
