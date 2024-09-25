#include <iostream>
#include <string>
#include <array>
#include <memory>

// Decorator function to associate URL with the ping function
void url_decorator(const std::string& url, std::string(*func)(const std::string&)) {
    std::string output = func(url);
    std::cout << "Ping output for URL " << url << ":\n" << output << std::endl;
}

// Function to run the ping command and return the output
std::string ping(const std::string& url) {
    std::string command = "ping -c 4 " + url; // Construct the ping command
    std::array<char, 128> buffer;
    std::string result;
    std::shared_ptr<FILE> pipe(popen(command.c_str(), "r"), pclose);
    if (!pipe) throw std::runtime_error("popen() failed!");
    while (fgets(buffer.data(), buffer.size(), pipe.get()) != nullptr) {
        result += buffer.data();
    }
    return result;
}

int main() {
    std::string url = "www.example.com";
    url_decorator(url, ping);
    return 0;
}