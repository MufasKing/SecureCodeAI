#include <iostream>
#include <string>
#include <map>

using namespace std;

// Simulating a database with a map
map<string, string> database = {
    {"user1", "password1"},
    {"user2", "password2"},
    {"user3", "password3"}
};

void redirectTo(const string& page) {
    cout << "Redirecting to: " << page << endl;
}

void login(const string& username, const string& password) {
    try {
        // Check if username exists in the database
        auto it = database.find(username);
        if (it != database.end()) {
            // Check if the password matches
            if (it->second == password) {
                redirectTo("success");
            } else {
                redirectTo("cant_login");
            }
        } else {
            redirectTo("cant_login");
        }
    } catch (const exception& e) {
        cout << "An error occurred: " << e.what() << endl;
        redirectTo("internal_server_error");
    }
}

int main() {
    string username;
    string password;

    cout << "Enter username: ";
    cin >> username;
    cout << "Enter password: ";
    cin >> password;

    login(username, password);

    return 0;
}
