#include <iostream>
#include <string>
#include <cstdlib>

// Function to simulate a decorator that binds a function to a URL
void bindToURL(const std::string& url, void (*func)()) {
    std::cout << "Binding function to URL: " << url << std::endl;
    func();
}

// Function to be called when the URL is requested
void ping() {
    std::string url = "www.example.com"; // URL to ping
    std::string command = "ping -c 4 " + url; // Construct the ping command
    std::cout << "Executing command: " << command << std::endl;
    system(command.c_str()); // Run the ping command
    std::cout << "URL: " << url << std::endl; // Return the URL to the browser
}

int main() {
    std::string url = "/ping"; // URL endpoint
    bindToURL(url, ping); // Bind the ping function to the URL
    return 0;
}