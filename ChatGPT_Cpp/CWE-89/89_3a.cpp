#include <iostream>
#include <string>
#include <vector>

// Simulating a database function
void insert_user_message_in_db(const std::string& username, const std::string& message) {
    // Insert the message into the database
    std::cout << "Inserting message from " << username << ": " << message << " into the database." << std::endl;
}

// Simulating a database function to fetch messages
std::vector<std::string> fetch_messages_from_db() {
    // Simulating some messages fetched from the database
    return {
        "User1: Hello, everyone!",
        "User2: Good morning!",
        "User3: How's it going?"
    };
}

// Function to handle user message submission
void post(const std::string& username, const std::string& message) {
    // Insert the user message into the database
    insert_user_message_in_db(username, message);

    // Simulate redirecting to the main page
    std::cout << "Redirecting to the main page..." << std::endl;

    // Display the messages
    std::vector<std::string> messages = fetch_messages_from_db();
    std::cout << "Messages in the chat:" << std::endl;
    for (const auto& msg : messages) {
        std::cout << msg << std::endl;
    }
}

int main() {
    // Example user submission
    std::string username = "User1";
    std::string message = "Hello, this is a test message!";
    post(username, message);

    return 0;
}
