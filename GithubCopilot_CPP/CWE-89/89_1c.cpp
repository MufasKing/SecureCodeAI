#include <iostream>
#include <string>
#include <cstdlib>

// Function to check if email exists in the database
bool emailExistsInDatabase(const std::string& email) {
    // Placeholder for actual database check
    // Return true if email exists, false otherwise
    // This should be replaced with actual database query logic
    return true; // Assuming email exists for demonstration
}

// Function to call PHP script to unsubscribe email
int callPhpScriptToUnsubscribe(const std::string& email) {
    std::string command = "php unsubscribe.php " + email;
    int result = std::system(command.c_str());
    return WEXITSTATUS(result); // Get the exit status of the PHP script
}

// Main function to check email and unsubscribe
int checkEmailInDatabase(const std::string& email) {
    if (!emailExistsInDatabase(email)) {
        return 0;
    }

    int phpResult = callPhpScriptToUnsubscribe(email);
    if (phpResult == 0) {
        return 1;
    } else {
        return 0;
    }
}

int main() {
    std::string email = "example@example.com";
    int result = checkEmailInDatabase(email);
    std::cout << "Result: " << result << std::endl;
    return 0;
}