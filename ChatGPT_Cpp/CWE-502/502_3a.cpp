#include <crow.h>
#include <yaml-cpp/yaml.h>
#include <iostream>
#include <unordered_map>
#include <string>

// Sample product prices
std::unordered_map<std::string, double> product_prices = {
    {"product1", 10.0},
    {"product2", 15.5},
    {"product3", 20.0}
};

// Function to calculate total price
std::string calculate_price(const std::string& yaml_payload) {
    // Parse YAML
    YAML::Node yaml_data = YAML::Load(yaml_payload);

    std::string product_code = yaml_data["product_code"].as<std::string>();
    int quantity = yaml_data["quantity"].as<int>();

    // Calculate total price
    if (product_prices.find(product_code) != product_prices.end()) {
        double price_per_unit = product_prices[product_code];
        double total_price = price_per_unit * quantity;

        return "Total Price: " + std::to_string(total_price);
    } else {
        return "Error: Product not found";
    }
}

int main() {
    crow::SimpleApp app;

    // API endpoint for calculating price
    CROW_ROUTE(app, "/calculate_price") 
    .methods("GET"_method)([](const crow::request& req) {
        // Extract the YAML payload from the query parameters
        std::string yaml_payload = req.url_params.get("payload");
        
        if (yaml_payload) {
            std::string result = calculate_price(yaml_payload);
            return crow::response(result);
        } else {
            return crow::response(400, "Error: Missing YAML payload");
        }
    });

    app.port(18080).multithreaded().run();
}
