#include <iostream>
#include <string>
#include <regex>
#include <cstdlib>

int main() {
    // Get the query parameter 'target'
    std::string target = std::getenv("QUERY_STRING");  // In a CGI environment, the query string is usually passed as an environment variable.

    // Regular expression to match the target variable
    std::regex target_regex("^[\\w\\-]+\\.$");  // Matches alphanumeric characters or hyphens followed by a period.

    // Check if the target matches the regex
    if (std::regex_match(target, target_regex)) {
        // Redirect to the target
        std::cout << "Status: 302 Found\r\n";
        std::cout << "Location: " << target << "\r\n\r\n";
    } else {
        // Redirect to the root of the site
        std::cout << "Status: 302 Found\r\n";
        std::cout << "Location: /\r\n\r\n";
    }

    return 0;
}
