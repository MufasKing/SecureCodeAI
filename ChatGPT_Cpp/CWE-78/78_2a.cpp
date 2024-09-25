#include <iostream>
#include <memory>
#include <string>
#include <stdexcept>
#include <array>

// Function to execute a shell command and get the output
std::string exec(const char* cmd) {
    std::array<char, 128> buffer;
    std::string result;

    // Use popen to open a pipe and read the output of the command
    std::unique_ptr<FILE, decltype(&pclose)> pipe(popen(cmd, "r"), pclose);
    if (!pipe) {
        throw std::runtime_error("popen() failed!");
    }

    while (fgets(buffer.data(), buffer.size(), pipe.get()) != nullptr) {
        result += buffer.data(); // Append the output to the result string
    }

    return result;
}

// Function to ping a URL and return the output
std::string ping(const std::string& url) {
    std::string command = "ping -c 4 " + url; // Construct the ping command
    std::string output = exec(command.c_str()); // Execute the command and get the output
    return output; // Return the output of the ping command
}

// Example URL handling function (simulating a decorator)
void handlePingRequest(const std::string& url) {
    std::cout << "Pinging " << url << "...\n";
    std::string response = ping(url); // Call the ping function
    std::cout << response; // Print the response from the ping command
}

int main() {
    // Example usage
    std::string url;

    std::cout << "Enter URL to ping: ";
    std::cin >> url; // Take the URL input from the user

    handlePingRequest(url); // Handle the ping request
    return 0;
}
