#include <iostream>
#include <string>
#include <stdexcept>

// Function to extract the domain from a URL
std::string extract_domain(const std::string& url) {
    std::string protocol = "://";
    size_t protocol_pos = url.find(protocol);
    if (protocol_pos == std::string::npos) {
        throw std::invalid_argument("Invalid URL format");
    }

    // Extract the domain from the URL
    size_t domain_start = protocol_pos + protocol.length();
    size_t domain_end = url.find('/', domain_start);
    std::string domain = url.substr(domain_start, domain_end - domain_start);

    return domain;
}

// Function to handle URL redirection
void redirect_url(const std::string& url) {
    try {
        // Extract the domain from the URL
        std::string domain = extract_domain(url);
        
        // Check if the domain is "example.com"
        if (domain == "example.com") {
            std::cout << "Redirecting to: " << url << std::endl;
        } else {
            // If the domain is not "example.com", return a 404 error
            std::cout << "404 Error: Page not found." << std::endl;
        }
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
}

int main() {
    // Test the redirect_url function
    std::string test_url1 = "https://example.com/path/to/resource";
    std::string test_url2 = "https://otherdomain.com/path/to/resource";
    
    std::cout << "Testing URL: " << test_url1 << std::endl;
    redirect_url(test_url1);
    
    std::cout << "\nTesting URL: " << test_url2 << std::endl;
    redirect_url(test_url2);
    
    return 0;
}
