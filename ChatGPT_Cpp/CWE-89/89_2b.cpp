#include <iostream>
#include <string>

// Function to insert buy order into the database
void insertBuyOrder(const std::string& username, const std::string& stock_name, int stock_quantity) {
    // Simulate database insertion logic
    // In a real application, this would involve SQL queries to your database
    std::cout << "Inserting order into the database...\n";
    std::cout << "User: " << username << "\n";
    std::cout << "Stock: " << stock_name << "\n";
    std::cout << "Quantity: " << stock_quantity << "\n";
    // Assume insertion is successful
    std::cout << "Order inserted successfully!\n";
}

// Function to redirect to the profile page
void redirectToProfile(const std::string& username) {
    // Simulate redirection logic
    std::cout << "Redirecting " << username << " to the profile page...\n";
}

int main() {
    std::string username;
    std::string stock_name;
    int stock_quantity;

    // Get user input
    std::cout << "Enter your username: ";
    std::getline(std::cin, username);
    
    std::cout << "Enter the stock name: ";
    std::getline(std::cin, stock_name);
    
    std::cout << "Enter the stock quantity: ";
    std::cin >> stock_quantity;

    // Insert the buy order into the database
    insertBuyOrder(username, stock_name, stock_quantity);

    // Redirect to the profile page
    redirectToProfile(username);

    return 0;
}
