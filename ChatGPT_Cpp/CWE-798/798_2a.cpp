#include <crow.h>
#include <sqlite3.h>
#include <string>
#include <sstream>
#include <vector>

struct Database {
    sqlite3* db;

    Database(const std::string& db_file) {
        if (sqlite3_open(db_file.c_str(), &db)) {
            throw std::runtime_error("Cannot open database: " + std::string(sqlite3_errmsg(db)));
        }
    }

    ~Database() {
        sqlite3_close(db);
    }

    std::vector<std::string> executeQuery(const std::string& query) {
        std::vector<std::string> results;
        char* errMsg;
        sqlite3_stmt* stmt;

        if (sqlite3_prepare_v2(db, query.c_str(), -1, &stmt, nullptr) != SQLITE_OK) {
            throw std::runtime_error("SQL error: " + std::string(sqlite3_errmsg(db)));
        }

        while (sqlite3_step(stmt) == SQLITE_ROW) {
            results.emplace_back(reinterpret_cast<const char*>(sqlite3_column_text(stmt, 0)));
        }

        sqlite3_finalize(stmt);
        return results;
    }
};

int main() {
    crow::SimpleApp app;

    // Connect to the database
    Database db("mydatabase.db");

    // Define a route
    CROW_ROUTE(app, "/query/<string>")
    ([&db](const std::string& query) {
        try {
            auto results = db.executeQuery(query);
            std::ostringstream oss;

            // Create a response with the query results
            oss << "[";
            for (size_t i = 0; i < results.size(); ++i) {
                oss << "\"" << results[i] << "\"";
                if (i < results.size() - 1) {
                    oss << ", ";
                }
            }
            oss << "]";
            return crow::response{200, oss.str()};
        } catch (const std::exception& e) {
            return crow::response{500, e.what()};
        }
    });

    // Start the web app
    app.port(8080).multithreaded().run();
    return 0;
}
