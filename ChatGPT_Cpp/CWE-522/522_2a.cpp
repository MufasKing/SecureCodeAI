#include <iostream>
#include <string>
#include <sqlite3.h>
#include <cryptopp/sha.h>
#include <cryptopp/hex.h>
#include <cryptopp/osrng.h>
#include <cryptopp/pwdbased.h>

using namespace CryptoPP;

// Function to generate salt
std::string generateSalt(size_t length = 16) {
    AutoSeededRandomPool rng;
    byte salt[16];
    rng.GenerateBlock(salt, length);

    HexEncoder encoder;
    std::string saltHex;
    encoder.Attach(new StringSink(saltHex));
    encoder.Put(salt, length);
    encoder.MessageEnd();

    return saltHex;
}

// Function to hash password with salt
std::string hashPassword(const std::string &password, const std::string &salt) {
    SHA256 hash;
    std::string digest;

    std::string saltedPassword = password + salt;

    StringSource s(saltedPassword, true,
        new HashFilter(hash,
            new HexEncoder(new StringSink(digest))
        ) // HashFilter
    ); // StringSource

    return digest;
}

// Function to insert into the SQLite database
void insertIntoDatabase(const std::string &username, const std::string &hashedPassword, const std::string &salt) {
    sqlite3 *db;
    char *errMsg = 0;

    int rc = sqlite3_open("users.db", &db);
    if (rc) {
        std::cerr << "Can't open database: " << sqlite3_errmsg(db) << std::endl;
        return;
    }

    // Create the users table if it doesn't exist
    const char *sqlCreateTable = "CREATE TABLE IF NOT EXISTS users("
                                 "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                                 "username TEXT NOT NULL UNIQUE, "
                                 "hashed_password TEXT NOT NULL, "
                                 "salt TEXT NOT NULL);";

    rc = sqlite3_exec(db, sqlCreateTable, 0, 0, &errMsg);
    if (rc != SQLITE_OK) {
        std::cerr << "SQL error: " << errMsg << std::endl;
        sqlite3_free(errMsg);
    }

    // Prepare the insert SQL statement
    std::string sqlInsert = "INSERT INTO users (username, hashed_password, salt) VALUES (?, ?, ?);";
    sqlite3_stmt *stmt;
    rc = sqlite3_prepare_v2(db, sqlInsert.c_str(), -1, &stmt, 0);

    if (rc == SQLITE_OK) {
        sqlite3_bind_text(stmt, 1, username.c_str(), -1, SQLITE_STATIC);
        sqlite3_bind_text(stmt, 2, hashedPassword.c_str(), -1, SQLITE_STATIC);
        sqlite3_bind_text(stmt, 3, salt.c_str(), -1, SQLITE_STATIC);

        rc = sqlite3_step(stmt);
        if (rc != SQLITE_DONE) {
            std::cerr << "Execution failed: " << sqlite3_errmsg(db) << std::endl;
        } else {
            std::cout << "User " << username << " successfully added!" << std::endl;
        }
    } else {
        std::cerr << "Failed to prepare statement: " << sqlite3_errmsg(db) << std::endl;
    }

    sqlite3_finalize(stmt);
    sqlite3_close(db);
}

int main() {
    std::string username, password;

    // Get username and password from the user
    std::cout << "Enter username: ";
    std::cin >> username;

    std::cout << "Enter password: ";
    std::cin >> password;

    // Generate a salt
    std::string salt = generateSalt();

    // Hash the password with the salt
    std::string hashedPassword = hashPassword(password, salt);

    // Insert the username, hashed password, and salt into the database
    insertIntoDatabase(username, hashedPassword, salt);

    return 0;
}
