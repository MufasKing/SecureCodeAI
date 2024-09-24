#include <iostream>
using namespace std;

void redirectUser(bool isLoggedIn, bool isAdmin) {
    if (!isLoggedIn) {
        cout << "Redirecting to login page..." << endl;
    } else if (isAdmin) {
        cout << "Redirecting to admin page..." << endl;
    } else {
        cout << "Redirecting to user page..." << endl;
    }
}

int main() {
    // Example usage
    bool isLoggedIn = false;
    bool isAdmin = false;

    // Test cases
    redirectUser(isLoggedIn, isAdmin); // Should redirect to login page

    isLoggedIn = true;
    redirectUser(isLoggedIn, isAdmin); // Should redirect to user page

    isAdmin = true;
    redirectUser(isLoggedIn, isAdmin); // Should redirect to admin page

    return 0;
}