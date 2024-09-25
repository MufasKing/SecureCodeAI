#include <iostream>
#include <string>

// Function to insert the user message into the database
void insert_user_message_in_db(const std::string& username, const std::string& message) {
    // Database insertion logic here
    std::cout << "Inserting message from " << username << " into the database: " << message << std::endl;
}

// Function to handle the post request
void post(const std::string& username, const std::string& message) {
    // Insert the message into the database
    insert_user_message_in_db(username, message);
    
    // Redirect to the main page
    std::cout << "Redirecting to the main page..." << std::endl;
}

// Main function to simulate the form submission
int main() {
    // Simulate form submission
    std::string username = "user1";
    std::string message = "Hello, this is a test message!";
    
    // Call the post function
    post(username, message);
    
    return 0;
}