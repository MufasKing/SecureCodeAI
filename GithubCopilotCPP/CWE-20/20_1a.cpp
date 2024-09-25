#include <iostream>
#include <regex>
#include <string>

// Define the regular expression as a constant
const std::regex target_url_regex("https://example\\.com/.*");

// Function to get the redirect URL
std::string getRedirectURL(const std::string& target_url) {
    // Default URL to use if the target URL does not match
    const std::string default_url = "https://default.com";

    // Check if the target URL matches the regular expression
    if (std::regex_match(target_url, target_url_regex)) {
        return target_url;
    } else {
        return default_url;
    }
}

int main() {
    std::string target_url = "https://example.com/page";
    std::string redirect_url = getRedirectURL(target_url);

    std::cout << "Redirect URL: " << redirect_url << std::endl;

    return 0;
}