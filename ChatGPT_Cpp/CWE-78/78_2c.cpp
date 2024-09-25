#include <iostream>
#include <string>
#include <cstdlib>
#include <memory>
#include <array>

class URLPinger {
public:
    explicit URLPinger(const std::string& url) : url(url) {}

    void ping() {
        std::string command = "ping -c 1 " + url + " > /dev/null 2>&1"; // For Unix-based systems
        int result = system(command.c_str());

        if (result == 0) {
            std::cout << "The URL " << url << " is alive." << std::endl;
        } else {
            std::cout << "The URL " << url << " is not alive." << std::endl;
        }
    }

private:
    std::string url;
};

int main() {
    std::string url = "example.com"; // Replace with the desired URL
    URLPinger pinger(url);
    pinger.ping();

    return 0;
}
