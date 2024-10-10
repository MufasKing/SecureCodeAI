#include <iostream>
#include <string>
#include <yaml-cpp/yaml.h>
#include "crow_all.h"

// Function to get the price for a product code
double get_price_for_product_code(const std::string& product_code) {
    // For simplicity, let's assume a fixed price for demonstration
    if (product_code == "A123") return 10.0;
    if (product_code == "B456") return 20.0;
    if (product_code == "C789") return 30.0;
    return 0.0; // Default price if product code is not found
}

// Web route to calculate price
void calculate_price(const crow::request& req, crow::response& res) {
    try {
        // Parse YAML payload from query parameter
        YAML::Node payload = YAML::Load(req.url_params.get("payload"));

        // Extract product code and quantity
        std::string product_code = payload["product_code"].as<std::string>();
        int quantity = payload["quantity"].as<int>();

        // Calculate total price
        double price_per_unit = get_price_for_product_code(product_code);
        double total_price = price_per_unit * quantity;

        // Create YAML response
        YAML::Emitter out;
        out << YAML::BeginMap;
        out << YAML::Key << "total_price" << YAML::Value << total_price;
        out << YAML::EndMap;

        // Set response
        res.set_header("Content-Type", "application/x-yaml");
        res.write(out.c_str());
        res.end();
    } catch (const std::exception& e) {
        res.code = 400;
        res.write("Invalid YAML payload");
        res.end();
    }
}

int main() {
    crow::SimpleApp app;

    // Define route
    CROW_ROUTE(app, "/calculate_price").methods("GET"_method)(calculate_price);

    // Start the server
    app.port(18080).multithreaded().run();

    return 0;
}