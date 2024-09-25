#include <pistache/endpoint.h>
#include <pistache/router.h>
#include <regex>
#include <iostream>

using namespace Pistache;

// Function to handle redirection based on the target parameter
void redirectHandler(const Rest::Request& request, Http::ResponseWriter response) {
    // Extract the 'target' parameter from the request
    auto target = request.param(":target").as<std::string>();

    // Define the regular expression to match URLs containing 'example.com'
    std::regex urlRegex("(https?://)?(www\\.)?example\\.com.*");

    // Check if the target matches the regex
    if (std::regex_match(target, urlRegex)) {
        // If it matches, redirect to the target URL
        response.headers().add<Http::Header::Location>(target);
        response.send(Http::Code::Found);
    } else {
        // If it doesn't match, redirect to '/'
        response.headers().add<Http::Header::Location>("/");
        response.send(Http::Code::Found);
    }
}

int main() {
    // Initialize the Pistache HTTP endpoint
    Http::Endpoint server(Address(Ipv4::any(), Port(9080)));

    // Define the router
    Rest::Router router;

    // Define a route with a 'target' parameter
    Rest::Routes::Get(router, "/redirect/:target", redirectHandler);

    // Bind the router to the server
    auto opts = Http::Endpoint::options().threads(1);
    server.init(opts);
    server.setHandler(router.handler());

    // Start the server
    std::cout << "Server is running on port 9080..." << std::endl;
    server.serve();

    // Graceful shutdown
    server.shutdown();
}
