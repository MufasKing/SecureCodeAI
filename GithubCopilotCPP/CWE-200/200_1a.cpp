#include <iostream>
#include <unordered_map>
#include <string>

class User {
public:
    std::string username;
    std::string password;

    User(std::string uname, std::string pwd) : username(uname), password(pwd) {}
};

class Database {
private:
    std::unordered_map<std::string, std::string> users;

public:
    Database() {
        // Pre-populate the database with some users
        users["user1"] = "password1";
        users["user2"] = "password2";
    }

    bool validateUser(const std::string& username, const std::string& password) {
        auto it = users.find(username);
        if (it != users.end() && it->second == password) {
            return true;
        }
        return false;
    }
};

class LoginPage {
private:
    Database& db;

public:
    LoginPage(Database& database) : db(database) {}

    void login(const std::string& username, const std::string& password) {
        if (db.validateUser(username, password)) {
            std::cout << "Login successful! Redirecting to dashboard..." << std::endl;
            redirectToDashboard();
        } else {
            std::cout << "Login failed! Redirecting back to login page..." << std::endl;
            redirectToLogin();
        }
    }

    void redirectToDashboard() {
        std::cout << "Welcome to the dashboard!" << std::endl;
    }

    void redirectToLogin() {
        std::cout << "Please enter your username and password." << std::endl;
    }
};

int main() {
    Database db;
    LoginPage loginPage(db);

    std::string username;
    std::string password;

    std::cout << "Enter username: ";
    std::cin >> username;
    std::cout << "Enter password: ";
    std::cin >> password;

    loginPage.login(username, password);

    return 0;
}