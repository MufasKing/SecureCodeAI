#include <iostream>
#include <string>
#include <unordered_map>
#include <functional>

// Function to escape special characters to HTML-safe sequences
std::string escape(const std::string& input) {
    std::string escaped;
    for (char c : input) {
        switch (c) {
            case '&': escaped += "&amp;"; break;
            case '<': escaped += "&lt;"; break;
            case '>': escaped += "&gt;"; break;
            case '"': escaped += "&quot;"; break;
            case '\'': escaped += "&#39;"; break;
            default: escaped += c; break;
        }
    }
    return escaped;
}

// URL mapping decorator
class URLMapper {
public:
    void add_mapping(const std::string& url, std::function<std::string(const std::string&)> func) {
        url_map[url] = func;
    }

    std::string call_function(const std::string& url, const std::string& arg) {
        if (url_map.find(url) != url_map.end()) {
            return url_map[url](arg);
        }
        return "404 Not Found";
    }

private:
    std::unordered_map<std::string, std::function<std::string(const std::string&)>> url_map;
};

// Function to be decorated
std::string hello(const std::string& username) {
    return "Hello " + escape(username);
}

int main() {
    URLMapper mapper;
    mapper.add_mapping("/hello/username", hello);

    // Simulate a user navigating to the URL /hello/username with the username "world"
    std::string response = mapper.call_function("/hello/username", "world");
    std::cout << response << std::endl;

    return 0;
}