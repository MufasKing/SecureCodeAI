#include <cpprest/http_listener.h>
#include <cpprest/yaml.h>
#include <cpprest/json.h>
#include <iostream>
#include <unordered_map>
#include <string>

// Function to return the price for a product code
double get_price_for_product_code(const std::string& product_code) {
    // Sample product prices
    std::unordered_map<std::string, double> product_prices = {
        {"product_1", 10.0},
        {"product_2", 15.5},
        {"product_3", 7.75}
    };

    auto it = product_prices.find(product_code);
    if (it != product_prices.end()) {
        return it->second;
    } else {
        return 0.0; // Product not found
    }
}

// Function to calculate total price from a YAML payload
double calculate_price(const std::string& yaml_payload) {
    // Load YAML into a dictionary
    YAML::Node data = YAML::Load(yaml_payload);
    std::string product_code = data["product_code"].as<std::string>();
    int quantity = data["quantity"].as<int>();

    // Get price for the product code
    double price_per_unit = get_price_for_product_code(product_code);
    return price_per_unit * quantity;
}

// Main function for the microservice
int main() {
    // Create an HTTP listener
    web::http::experimental::listener::http_listener listener("http://localhost:8080/calculate_price");

    listener.support(web::http::methods::POST, [](web::http::http_request request) {
        request.extract_string().then([=](const std::string& body) {
            // Calculate the total price
            double total_price = calculate_price(body);

            // Prepare the YAML response
            YAML::Node response;
            response["total_price"] = total_price;

            // Send the response
            request.reply(web::http::status_codes::OK, YAML::Dump(response));
        }).wait();
    });

    // Start the listener
    try {
        listener
            .open()
            .then([](){ std::cout << "Starting to listen at: http://localhost:8080/calculate_price" << std::endl; })
            .wait();

        std::string line;
        std::getline(std::cin, line); // Keep the service running
    } catch (const std::exception& e) {
        std::cerr << "An error occurred: " << e.what() << std::endl;
    }

    return 0;
}
