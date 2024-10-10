#include <iostream>
#include <fstream>
#include <string>

// Mock decorator function to associate URL with function
void route(const std::string& url, std::function<void(const std::string&)> func) {
    // In a real web framework, this would register the URL and function
    std::cout << "Route registered: " << url << std::endl;
}

// Function to handle image requests
void img(const std::string& name) {
    std::string filePath = "images/" + name;
    std::ifstream file(filePath, std::ios::binary);

    if (!file) {
        std::cerr << "File not found: " << filePath << std::endl;
        return;
    }

    std::cout << "Sending file: " << filePath << std::endl;
    // Mock sending file to browser
    std::cout << file.rdbuf();
}

int main() {
    // Register the img function with the /img URL
    route("/img", img);

    // Example usage
    img("example.jpg");

    return 0;
}