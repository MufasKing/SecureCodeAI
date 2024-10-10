#include "crow.h"

// Function to get the price for a product code
double getPriceForProductCode(const std::string& productCode) {
    // Example pricing logic
    if (productCode == "A123") {
        return 10.0;
    } else if (productCode == "B456") {
        return 20.0;
    } else if (productCode == "C789") {
        return 30.0;
    } else {
        return 0.0; // Default price for unknown product codes
    }
}

int main() {
    crow::SimpleApp app;

    // Define a route that calculates the price for a product code and quantity
    CROW_ROUTE(app, "/price/<string>/<int>")
    ([](const std::string& productCode, int quantity) {
        double price = getPriceForProductCode(productCode);
        double totalPrice = price * quantity;
        return crow::response(std::to_string(totalPrice));
    });

    // Run the app on port 5000
    app.port(5000).multithreaded().run();

    return 0;
}