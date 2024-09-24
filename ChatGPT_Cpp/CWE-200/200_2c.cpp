#include <iostream>
#include <string>

using namespace std;

// Function to simulate the session page
void sessionPage() {
    cout << "Welcome to the session page!" << endl;
}

// Main function
int main() {
    string username;
    string password;

    // Predefined credentials
    const string correctUsername = "admin";
    const string correctPassword = "password123";

    cout << "Login Page" << endl;
    cout << "-----------" << endl;

    // Prompt for username
    cout << "Enter username: ";
    getline(cin, username);

    // Prompt for password
    cout << "Enter password: ";
    getline(cin, password);

    // Check credentials
    if (username == correctUsername && password == correctPassword) {
        sessionPage(); // Redirect to session page
    } else {
        cout << "Incorrect username or password." << endl; // Error message
    }

    return 0;
}
