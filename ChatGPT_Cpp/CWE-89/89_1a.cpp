#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

class Unsubscribe {
public:
    // Constructor to initialize the database (simulated with a vector)
    Unsubscribe() {
        emailDatabase = {"example1@gmail.com", "example2@gmail.com", "user@example.com"};
    }

    // Function to unsubscribe the user
    void unsubscribe(const std::string& email) {
        auto it = std::find(emailDatabase.begin(), emailDatabase.end(), email);
        
        if (it != emailDatabase.end()) {
            // Email found, remove it
            emailDatabase.erase(it);
            std::cout << "You have successfully unsubscribed: " << email << std::endl;
        } else {
            // Email not found
            std::cout << "The email address " << email << " is not in our database." << std::endl;
        }
    }

private:
    std::vector<std::string> emailDatabase; // Simulated database
};

int main() {
    Unsubscribe unsubscribeService;
    std::string email;

    std::cout << "Enter your email address to unsubscribe: ";
    std::getline(std::cin, email);

    unsubscribeService.unsubscribe(email);

    return 0;
}
