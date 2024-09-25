#include <iostream>
#include <string>
#include <cstdlib> // For system()

// Simulated database check function
bool emailExistsInDatabase(const std::string& email) {
    // Replace this logic with actual database query
    // For demonstration, let's assume "test@example.com" exists
    return (email == "test@example.com");
}

// Function to call the PHP script
int callUnsubscribeScript(const std::string& email) {
    // Replace with actual call to the PHP script
    // For demonstration, we will simulate a successful unsubscribe
    std::string command = "php unsubscribe.php " + email; // Adjust path as needed
    int result = system(command.c_str()); // Execute the PHP script

    // Simulate the PHP script returning 0 or 1
    // Let's say 0 means success and 1 means failure
    return (result == 0) ? 0 : 1; // Simulate PHP success/failure
}

// Main function to check email and unsubscribe
int checkAndUnsubscribeEmail(const std::string& email) {
    if (!emailExistsInDatabase(email)) {
        return 0; // Email does not exist
    }

    // Email exists, call the unsubscribe script
    int result = callUnsubscribeScript(email);
    
    // Return 1 if PHP script succeeded, otherwise return 0
    return (result == 0) ? 1 : 0;
}

int main() {
    std::string email;
    
    std::cout << "Enter the email to unsubscribe: ";
    std::cin >> email;

    int result = checkAndUnsubscribeEmail(email);
    
    if (result == 0) {
        std::cout << "Unsubscribe failed or email does not exist." << std::endl;
    } else {
        std::cout << "Successfully unsubscribed." << std::endl;
    }

    return 0;
}
