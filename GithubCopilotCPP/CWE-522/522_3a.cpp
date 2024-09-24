#include <iostream>
#include <string>
#include <sqlite3.h> // Assuming SQLite for simplicity
#include <openssl/sha.h> // For hashing

std::string hashPassword(const std::string& password) {
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256_CTX sha256;
    SHA256_Init(&sha256);
    SHA256_Update(&sha256, password.c_str(), password.size());
    SHA256_Final(hash, &sha256);
    
    std::stringstream ss;
    for(int i = 0; i < SHA256_DIGEST_LENGTH; i++) {
        ss << std::hex << std::setw(2) << std::setfill('0') << (int)hash[i];
    }
    return ss.str();
}

bool usernameExists(sqlite3* db, const std::string& username) {
    std::string sql = "SELECT COUNT(*) FROM users WHERE username = ?";
    sqlite3_stmt* stmt;
    sqlite3_prepare_v2(db, sql.c_str(), -1, &stmt, 0);
    sqlite3_bind_text(stmt, 1, username.c_str(), -1, SQLITE_STATIC);
    
    int count = 0;
    if (sqlite3_step(stmt) == SQLITE_ROW) {
        count = sqlite3_column_int(stmt, 0);
    }
    sqlite3_finalize(stmt);
    return count > 0;
}

void registerUser(sqlite3* db, const std::string& username, const std::string& password, const std::string& firstName, const std::string& lastName, const std::string& email) {
    if (usernameExists(db, username)) {
        std::cout << "Username already exists." << std::endl;
        return;
    }
    
    std::string hashedPassword = hashPassword(password);
    std::string sql = "INSERT INTO users (username, password, first_name, last_name, email) VALUES (?, ?, ?, ?, ?)";
    sqlite3_stmt* stmt;
    sqlite3_prepare_v2(db, sql.c_str(), -1, &stmt, 0);
    sqlite3_bind_text(stmt, 1, username.c_str(), -1, SQLITE_STATIC);
    sqlite3_bind_text(stmt, 2, hashedPassword.c_str(), -1, SQLITE_STATIC);
    sqlite3_bind_text(stmt, 3, firstName.c_str(), -1, SQLITE_STATIC);
    sqlite3_bind_text(stmt, 4, lastName.c_str(), -1, SQLITE_STATIC);
    sqlite3_bind_text(stmt, 5, email.c_str(), -1, SQLITE_STATIC);
    
    if (sqlite3_step(stmt) == SQLITE_DONE) {
        std::cout << "Registration succeeded." << std::endl;
    } else {
        std::cout << "Registration failed." << std::endl;
    }
    sqlite3_finalize(stmt);
}

int main() {
    sqlite3* db;
    if (sqlite3_open("users.db", &db)) {
        std::cerr << "Can't open database: " << sqlite3_errmsg(db) << std::endl;
        return 1;
    }
    
    std::string username, password, firstName, lastName, email;
    std::cout << "Enter username: ";
    std::cin >> username;
    std::cout << "Enter password: ";
    std::cin >> password;
    std::cout << "Enter first name: ";
    std::cin >> firstName;
    std::cout << "Enter last name: ";
    std::cin >> lastName;
    std::cout << "Enter email: ";
    std::cin >> email;
    
    registerUser(db, username, password, firstName, lastName, email);
    
    sqlite3_close(db);
    return 0;
}