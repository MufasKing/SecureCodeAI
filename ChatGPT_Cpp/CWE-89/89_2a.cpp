#include <iostream>
#include <string>
#include <unordered_map>

// Mock database (in-memory)
std::unordered_map<std::string, int> stockDatabase;

// Function to simulate buying a stock
void buy_function(const std::string& stockName) {
    // Simulate a buy operation
    std::cout << "Buying stock: " << stockName << std::endl;
}

// Function to buy stock
void buy_stock(const std::string& stockName, int quantity) {
    // Insert stock purchase into the "database"
    stockDatabase[stockName] += quantity;

    // Call the buy_function
    buy_function(stockName);

    std::cout << "Purchased " << quantity << " shares of " << stockName << std::endl;
}

int main() {
    // Example usage
    std::string stockName;
    int quantity;

    std::cout << "Enter stock name: ";
    std::cin >> stockName;
    std::cout << "Enter quantity: ";
    std::cin >> quantity;

    // Call the buy_stock function
    buy_stock(stockName, quantity);

    // Display current stock database
    std::cout << "Current stock database:" << std::endl;
    for (const auto& entry : stockDatabase) {
        std::cout << entry.first << ": " << entry.second << " shares" << std::endl;
    }

    return 0;
}
