#include <iostream>
#include <fstream>
#include <filesystem>
#include <string>
#include <functional>

// Decorator type definition
using UrlDecorator = std::function<void()>;

class ImageHandler {
public:
    // The decorator that specifies the URL for the handler
    static void RegisterHandler(const std::string& url, UrlDecorator handler) {
        handlers[url] = handler;
    }

    // Function to invoke the handler based on URL
    static void HandleRequest(const std::string& url) {
        if (handlers.find(url) != handlers.end()) {
            handlers[url]();
        } else {
            std::cout << "404 Not Found: The requested URL was not found on this server." << std::endl;
        }
    }

private:
    static std::map<std::string, UrlDecorator> handlers;  // URL handlers map
};

std::map<std::string, UrlDecorator> ImageHandler::handlers;

// Function to check if the file exists
bool fileExists(const std::string& path) {
    return std::filesystem::exists(path);
}

// Function to serve the image
void serveImage(const std::string& filename) {
    std::string path = "images/" + filename;

    if (fileExists(path)) {
        std::cout << "Serving file: " << path << std::endl;
        // Here, you would implement the logic to send the file to the browser.
        // For simplicity, we will just print a message.
    } else {
        std::cout << "404 Not Found: The file " << filename << " does not exist." << std::endl;
    }
}

// Example usage
int main() {
    // Register a URL for serving images
    ImageHandler::RegisterHandler("/images/sample.jpg", []() { serveImage("sample.jpg"); });

    // Simulate a request for the image
    ImageHandler::HandleRequest("/images/sample.jpg"); // Change this to test other paths

    return 0;
}
