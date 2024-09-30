#include <iostream>
#include <boost/asio.hpp>
#include <boost/beast.hpp>
#include <boost/beast/http.hpp>
#include <yaml-cpp/yaml.h>
#include <regex>

namespace beast = boost::beast;
namespace http = beast::http;
namespace net = boost::asio;
using tcp = net::ip::tcp;

// Input sanitization for the YAML payload
std::string sanitize_input(const std::string& input) {
    // Remove any potential harmful characters from input
    std::string sanitized_input = input;
    sanitized_input = std::regex_replace(sanitized_input, std::regex("<"), "&lt;");
    sanitized_input = std::regex_replace(sanitized_input, std::regex(">"), "&gt;");
    // Add further sanitization as needed (like SQL injection prevention)
    return sanitized_input;
}

// Input validation
bool is_valid_input(const std::string& payload) {
    // Perform basic validation checks (e.g., max length, structure, etc.)
    if (payload.size() > 10000) { // Limit the payload size
        return false;
    }
    return true;
}

// Secure YAML parsing (avoiding certain exploits)
YAML::Node secure_parse_yaml(const std::string& payload) {
    try {
        YAML::Node node = YAML::Load(payload);
        return node;
    } catch (const YAML::ParserException& ex) {
        throw std::runtime_error("YAML Parsing Error");
    }
}

// Handles incoming HTTP requests
void handle_request(http::request<http::string_body> req, http::response<http::string_body>& res) {
    if (req.method() != http::verb::post) {
        res.result(http::status::bad_request);
        res.body() = "Only POST method is supported.";
        return;
    }

    // Extract 'payload' from the request
    std::string payload;
    try {
        auto params = http::parse_query_string(req.body());
        if (params.find("payload") != params.end()) {
            payload = params.at("payload");
        } else {
            res.result(http::status::bad_request);
            res.body() = "Missing 'payload' parameter.";
            return;
        }
    } catch (std::exception& e) {
        res.result(http::status::bad_request);
        res.body() = "Error parsing query.";
        return;
    }

    // Input Validation and Sanitization
    if (!is_valid_input(payload)) {
        res.result(http::status::bad_request);
        res.body() = "Invalid payload.";
        return;
    }
    payload = sanitize_input(payload);

    // Secure YAML Parsing
    YAML::Node yaml_node;
    try {
        yaml_node = secure_parse_yaml(payload);
    } catch (const std::exception& e) {
        res.result(http::status::bad_request);
        res.body() = "Failed to parse YAML.";
        return;
    }

    // Check if 'type' exists in the YAML payload
    if (!yaml_node["type"]) {
        res.result(http::status::bad_request);
        res.body() = "Missing 'type' field in payload.";
        return;
    }

    std::string type = yaml_node["type"].as<std::string>();

    if (type == "Create") {
        res.result(http::status::bad_request);
        res.body() = "'Create' type is not allowed.";
    } else if (type == "Update") {
        if (yaml_node["name"] && yaml_node["name"].as<std::string>() == "UnsafeDeserialization") {
            res.result(http::status::ok);
            res.body() = "Update type with UnsafeDeserialization name.";
        } else {
            res.result(http::status::bad_request);
            res.body() = "'name' field must be 'UnsafeDeserialization' for Update type.";
        }
    } else {
        res.result(http::status::bad_request);
        res.body() = "Invalid 'type' field in payload.";
    }
}

// Server function
void server() {
    try {
        net::io_context ioc{1};
        tcp::acceptor acceptor{ioc, tcp::endpoint{tcp::v4(), 5000}};

        while (true) {
            tcp::socket socket{ioc};
            acceptor.accept(socket);

            // Handle the connection
            beast::flat_buffer buffer;
            http::request<http::string_body> req;
            http::read(socket, buffer, req);

            http::response<http::string_body> res{http::status::ok, req.version()};
            res.set(http::field::server, "BeastServer");
            res.keep_alive(req.keep_alive());

            handle_request(req, res);

            // Send the response
            http::write(socket, res);
        }
    } catch (std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
}

int main() {
    std::cout << "Starting server on port 5000...\n";
    server();
    return 0;
}
