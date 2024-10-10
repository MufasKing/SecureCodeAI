#include <crow.h>
#include <yaml-cpp/yaml.h>
#include <string>
#include <unordered_map>

// Function to get the price of a product based on product_code
double get_product_price(const std::string& product_code) {
    std::unordered_map<std::string, double> product_prices = {
        {"product1", 10.0},
        {"product2", 20.0},
        {"product3", 30.0}
    };
    return product_prices[product_code];
}

// Function to parse YAML payload and extract product_code and quantity
std::pair<std::string, int> parse_yaml_payload(const std::string& yaml_payload) {
    YAML::Node node = YAML::Load(yaml_payload);
    std::string product_code = node["product_code"].as<std::string>();
    int quantity = node["quantity"].as<int>();
    return {product_code, quantity};
}

// Entry point for the API
std::string calculate_price(const std::string& yaml_payload) {
    auto [product_code, quantity] = parse_yaml_payload(yaml_payload);
    double price = get_product_price(product_code);
    double total_price = price * quantity;
    return std::to_string(total_price);
}

int main() {
    crow::SimpleApp app;

    CROW_ROUTE(app, "/calculate_price")
    ([](const crow::request& req) {
        std::string yaml_payload = req.url_params.get("payload");
        std::string total_price = calculate_price(yaml_payload);
        return crow::response(total_price);
    });

    app.port(18080).multithreaded().run();
}