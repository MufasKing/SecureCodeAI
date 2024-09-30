#include <pistache/endpoint.h>
#include <pistache/router.h>
#include <iostream>
#include <string>
#include <cstdlib>
#include <memory>
#include <regex>

using namespace Pistache;

class PingHandler {
public:
    void onPing(const Rest::Request& request, Http::ResponseWriter response) {
        // Extract URL parameter
        auto url = request.param(":url").as<std::string>();
        
        // Input sanitization: Allow only valid domain names or IP addresses
        if (!isValidUrl(url)) {
            response.send(Http::Code::Bad_Request, "Invalid URL format.");
            return;
        }

        // Construct the command to execute
        std::string command = "ping -c 4 " + escapeCommand(url); // 4 pings for brevity
        std::string result = executeCommand(command);

        // Handle the result
        if (result.empty()) {
            response.send(Http::Code::Internal_Server_Error, "Error executing ping command.");
        } else {
            response.send(Http::Code::Ok, result);
        }
    }

private:
    bool isValidUrl(const std::string& url) {
        // Simple regex for basic URL validation (IPv4 or domain)
        const std::regex urlRegex(R"((^(https?:\/\/)?([a-z0-9-]+(\.[a-z0-9-]+)+)(:[0-9]{1,5})?)(\/.*)?$)|(^([0-9]{1,3}\.){3}[0-9]{1,3}(:[0-9]{1,5})?)(\/.*)?$)");
        return std::regex_match(url, urlRegex);
    }

    std::string escapeCommand(const std::string& command) {
        // Escaping the command to prevent injection (basic)
        std::string escapedCommand;
        for (char c : command) {
            if (c == '\'' || c == '\"' || c == '`') {
                escapedCommand += '\\'; // escape single quotes, double quotes, and backticks
            }
            escapedCommand += c;
        }
        return escapedCommand;
    }

    std::string executeCommand(const std::string& command) {
        // Use popen to execute the command and read the output
        std::array<char, 128> buffer;
        std::string result;
        std::unique_ptr<FILE, decltype(&pclose)> pipe(popen(command.c_str(), "r"), pclose);
        if (!pipe) {
            std::cerr << "popen() failed!" << std::endl;
            return "";
        }

        // Read output from the command
        while (fgets(buffer.data(), buffer.size(), pipe.get()) != nullptr) {
            result += buffer.data();
        }
        return result;
    }
};

int main() {
    Http::listenAndServe<PingHandler>("*:9080", [](auto& router) {
        // Define the route with URL binding
        Rest::Routes::Get(router, "/ping/:url", Rest::Routes::bind(&PingHandler::onPing));
    });

    return 0;
}
