#include <iostream>
#include <regex>
#include <string>

class URLRedirector {
public:
    URLRedirector(const std::string& regexPattern, const std::string& defaultUrl)
        : regexPattern(regexPattern), defaultUrl(defaultUrl), regexCompiled(regexPattern)
    {
        // Regular expression compiled when the object (module) is initialized
        std::cout << "Regex compiled with pattern: " << regexPattern << std::endl;
    }

    std::string getRedirectUrl(const std::string& targetUrl) const {
        // Match the target URL against the compiled regular expression
        if (std::regex_match(targetUrl, regexCompiled)) {
            std::cout << "URL matches: " << targetUrl << std::endl;
            return targetUrl; // Use the target URL as the redirect target
        } else {
            std::cout << "URL does not match, using default URL." << std::endl;
            return defaultUrl; // Use the default URL as the fallback
        }
    }

private:
    std::string regexPattern;
    std::string defaultUrl;
    std::regex regexCompiled; // The compiled regular expression
};

int main() {
    // Example of using the URLRedirector
    std::string regexPattern = R"(https:\/\/www\.example\.com\/[a-z]+)"; // Example regex pattern
    std::string defaultUrl = "https://www.default.com"; // Default fallback URL

    URLRedirector redirector(regexPattern, defaultUrl);

    std::string targetUrl1 = "https://www.example.com/home"; // This should match the regex
    std::string targetUrl2 = "https://www.nonmatching.com";  // This should not match the regex

    std::cout << "Redirect URL 1: " << redirector.getRedirectUrl(targetUrl1) << std::endl;
    std::cout << "Redirect URL 2: " << redirector.getRedirectUrl(targetUrl2) << std::endl;

    return 0;
}
