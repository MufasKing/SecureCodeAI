#include <iostream>
#include <string>

// Simulate database insertion
void insert_into_database(const std::string& stock_name, int quantity) {
    std::cout << "Inserting into database: " << stock_name << " with quantity " << quantity << std::endl;
}

// Function to be called after buying stock
void buy_function(const std::string& stock_name) {
    std::cout << "Executing buy_function for stock: " << stock_name << std::endl;
}

// Function to handle buying stock
void buy_stock(const std::string& stock_name, int quantity) {
    // Insert stock name and quantity into the database
    insert_into_database(stock_name, quantity);
    
    // Call buy_function with the stock name
    buy_function(stock_name);
}

int main() {
    // Example usage
    buy_stock("AAPL", 10);
    return 0;
}