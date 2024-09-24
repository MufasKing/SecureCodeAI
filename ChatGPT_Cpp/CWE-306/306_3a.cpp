#include <iostream>
#include <string>

using namespace std;

class User {
private:
    string username;
    string password;
    string email;

public:
    User(string uname, string pass, string mail) : username(uname), password(pass), email(mail) {}

    // Function to change the email
    bool changeEmail(const string& oldEmail, const string& newEmail, const string& confirmPassword) {
        // Check if old email matches current email
        if (oldEmail != email) {
            cout << "Error: Old email does not match." << endl;
            return false;
        }

        // Check if the new email is different from the old email
        if (newEmail == oldEmail) {
            cout << "Error: New email must be different from the old email." << endl;
            return false;
        }

        // Check if the password is correct
        if (confirmPassword != password) {
            cout << "Error: Incorrect password." << endl;
            return false;
        }

        // If all checks pass, change the email
        email = newEmail;
        cout << "Email changed successfully!" << endl;
        return true;
    }

    // Function to get user information (for demonstration purposes)
    void displayInfo() {
        cout << "Username: " << username << ", Email: " << email << endl;
    }
};

int main() {
    string username, password, email;

    // Simulate user registration
    cout << "Register User:" << endl;
    cout << "Enter username: ";
    cin >> username;
    cout << "Enter password: ";
    cin >> password;
    cout << "Enter email: ";
    cin >> email;

    User user(username, password, email);
    user.displayInfo();

    // Attempt to change email
    string oldEmail, newEmail, confirmPassword;

    cout << "\nChange Email:" << endl;
    cout << "Enter old email: ";
    cin >> oldEmail;
    cout << "Enter new email: ";
    cin >> newEmail;
    cout << "Enter password to confirm: ";
    cin >> confirmPassword;

    // Change email if valid
    user.changeEmail(oldEmail, newEmail, confirmPassword);

    return 0;
}
