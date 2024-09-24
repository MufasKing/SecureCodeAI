#include <iostream>
#include <string>
#include <unordered_map>
#include <openssl/sha.h>
#include <openssl/rand.h>
#include <sstream>
#include <iomanip>

using namespace std;

// Database to store username, salt, and hashed password
unordered_map<string, pair<string, string>> database;

// Function to convert binary data to hexadecimal string
string toHex(const unsigned char* data, size_t length) {
    stringstream ss;
    for (size_t i = 0; i < length; ++i)
        ss << hex << setw(2) << setfill('0') << (int)data[i];
    return ss.str();
}

// Function to generate a random salt
string generateSalt() {
    unsigned char salt[16];
    if (!RAND_bytes(salt, sizeof(salt))) {
        cerr << "Error generating random salt!" << endl;
        exit(EXIT_FAILURE);
    }
    return toHex(salt, sizeof(salt));
}

// Function to hash a password with a given salt
string hashPassword(const string& password, const string& salt) {
    string saltedPassword = password + salt;
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256((unsigned char*)saltedPassword.c_str(), saltedPassword.length(), hash);
    return toHex(hash, SHA256_DIGEST_LENGTH);
}

// Function to register a user
void registerUser() {
    string username, password;
    cout << "Register a new user\nUsername: ";
    cin >> username;
    cout << "Password: ";
    cin >> password;

    if (database.find(username) != database.end()) {
        cout << "Username already exists. Try a different one." << endl;
        return;
    }

    string salt = generateSalt();
    string hashedPassword = hashPassword(password, salt);
    database[username] = {salt, hashedPassword};

    cout << "User registered successfully!" << endl;
}

// Function to login a user
void loginUser() {
    string username, password;
    cout << "Login\nUsername: ";
    cin >> username;
    cout << "Password: ";
    cin >> password;

    if (database.find(username) == database.end()) {
        cout << "Invalid username!" << endl;
        return;
    }

    string salt = database[username].first;
    string storedHash = database[username].second;
    string hashedPassword = hashPassword(password, salt);

    if (hashedPassword == storedHash) {
        cout << "Login successful!" << endl;
    } else {
        cout << "Invalid password!" << endl;
    }
}

int main() {
    int choice;
    do {
        cout << "\n1. Register\n2. Login\n3. Exit\nChoice: ";
        cin >> choice;

        switch (choice) {
        case 1:
            registerUser();
            break;
        case 2:
            loginUser();
            break;
        case 3:
            cout << "Exiting..." << endl;
            break;
        default:
            cout << "Invalid choice. Try again." << endl;
        }
    } while (choice != 3);

    return 0;
}
