#include "crow_all.h"
#include <unordered_map>
#include <string>

double getPrice(const std::string& productCode) {
    // Define product prices
    std::unordered_map<std::string, double> productPrices = {
        {"A001", 10.0},
        {"A002", 15.5},
        {"A003", 7.25},
        {"B001", 20.0},
        {"B002", 25.0}
    };

    // Return the price if the product code exists, otherwise return 0
    auto it = productPrices.find(productCode);
    if (it != productPrices.end()) {
        return it->second;
    }
    return 0.0;
}

int main() {
    crow::SimpleApp app;

    // Route for calculating the price based on product code and quantity
    CROW_ROUTE(app, "/calculate/<string>/<int>")
    ([&](const crow::request& req, const std::string& productCode, int quantity) {
        double pricePerUnit = getPrice(productCode);
        double totalPrice = pricePerUnit * quantity;
        
        crow::json::wvalue response;
        response["productCode"] = productCode;
        response["quantity"] = quantity;
        response["pricePerUnit"] = pricePerUnit;
        response["totalPrice"] = totalPrice;

        return response;
    });

    // Start the app on port 5000
    app.port(5000).multithreaded().run();
}
