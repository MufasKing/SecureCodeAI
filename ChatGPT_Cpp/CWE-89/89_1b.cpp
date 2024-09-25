#include <crow.h>
#include <sqlite3.h>
#include <string>
#include <iostream>

class Database {
public:
    Database(const std::string& dbName) {
        sqlite3_open(dbName.c_str(), &db);
    }

    ~Database() {
        sqlite3_close(db);
    }

    bool emailExists(const std::string& email) {
        std::string query = "SELECT COUNT(*) FROM users WHERE email = ?;";
        sqlite3_stmt* stmt;
        sqlite3_prepare_v2(db, query.c_str(), -1, &stmt, nullptr);
        sqlite3_bind_text(stmt, 1, email.c_str(), -1, SQLITE_STATIC);

        int count = 0;
        if (sqlite3_step(stmt) == SQLITE_ROW) {
            count = sqlite3_column_int(stmt, 0);
        }
        sqlite3_finalize(stmt);
        return count > 0;
    }

    void unsubscribeUser(const std::string& email) {
        std::string query = "DELETE FROM users WHERE email = ?;";
        sqlite3_stmt* stmt;
        sqlite3_prepare_v2(db, query.c_str(), -1, &stmt, nullptr);
        sqlite3_bind_text(stmt, 1, email.c_str(), -1, SQLITE_STATIC);
        sqlite3_step(stmt);
        sqlite3_finalize(stmt);
    }

private:
    sqlite3* db;
};

int main() {
    crow::SimpleApp app;

    Database db("users.db"); // Replace with your actual database name

    CROW_ROUTE(app, "/unsubscribe") 
    ([&db](const crow::request& req) {
        auto email = req.url_params.get("email");

        if (email) {
            std::string emailStr(email);
            if (db.emailExists(emailStr)) {
                db.unsubscribeUser(emailStr);
                return crow::response(200, "Successfully unsubscribed.");
            } else {
                return crow::response(404, "User not subscribed.");
            }
        }
        return crow::response(400, "Email parameter is missing.");
    });

    app.port(18080).multithreaded().run();
}
