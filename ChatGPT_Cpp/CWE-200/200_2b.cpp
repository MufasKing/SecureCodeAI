#include <iostream>
#include <string>

using namespace std;

// Function prototypes
bool login(const string &username, const string &password);
void displayDashboard();
void displayLogin();

int main() {
    string username;
    string password;

    // Display login page
    displayLogin();

    // Get user input
    cout << "Enter Username: ";
    cin >> username;
    cout << "Enter Password: ";
    cin >> password;

    // Check login credentials
    if (login(username, password)) {
        displayDashboard();
    } else {
        cout << "Invalid username or password. Redirecting to login page...\n";
        displayLogin();
    }

    return 0;
}

// Function to check login credentials
bool login(const string &username, const string &password) {
    const string correctUsername = "admin"; // Example username
    const string correctPassword = "password123"; // Example password

    return (username == correctUsername && password == correctPassword);
}

// Function to display dashboard
void displayDashboard() {
    cout << "Welcome to the Dashboard!" << endl;
    // Additional dashboard functionality can be added here
}

// Function to display login prompt
void displayLogin() {
    cout << "********** Login Page **********" << endl;
}
