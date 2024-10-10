#include <iostream>
#include <string>
#include <cstdlib>

std::string url = "www.example.com";

void ping() {
    std::string command = "ping -c 1 " + url + " > /dev/null 2>&1";
    int result = system(command.c_str());
    std::string pong = (result == 0) ? "URL is alive" : "URL is not alive";
    std::cout << pong << std::endl;
}

int main() {
    ping();
    return 0;
}