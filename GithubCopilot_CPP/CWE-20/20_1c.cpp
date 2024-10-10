#include <iostream>
#include <regex>
#include <string>

// Function to simulate redirection
void redirect(const std::string& url) {
    std::cout << "Redirecting to: " << url << std::endl;
}

int main() {
    // Define the regular expression pattern
    std::regex pattern(R"(^[\w-]+\.$)");

    // Simulate retrieving the target query parameter
    std::string target = "example."; // This should be replaced with actual query parameter retrieval logic

    // Check if the target matches the regular expression
    if (std::regex_match(target, pattern)) {
        // Redirect to the target
        redirect(target);
    } else {
        // Redirect to the root of the site
        redirect("/");
    }

    return 0;
}