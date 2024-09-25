#include <iostream>
#include <string>
#include <regex>

// Function to parse the URL and extract the domain name
std::string get_domain_name(const std::string& url) {
    std::regex url_regex(R"((http|https)://([^/]+))");
    std::smatch url_match_result;
    if (std::regex_search(url, url_match_result, url_regex) && url_match_result.size() > 2) {
        return url_match_result[2].str();
    }
    return "";
}

// Function to redirect URL or return 404 error
void redirect_url(const std::string& url) {
    std::string domain_name = get_domain_name(url);
    if (domain_name == "example.com") {
        std::cout << "Redirecting to " << url << std::endl;
    } else {
        std::cout << "404 Error: Page not found" << std::endl;
    }
}

int main() {
    std::string url = "http://example.com/somepage";
    redirect_url(url);
    return 0;
}