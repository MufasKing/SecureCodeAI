#include <crow.h>
#include <sqlite3.h>
#include <string>
#include <iostream>

void createTableIfNotExists(sqlite3* db) {
    const char* sql = R"(
        CREATE TABLE IF NOT EXISTS stock_orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            stock_name TEXT NOT NULL,
            quantity INTEGER NOT NULL
        );
    )";

    char* errMsg;
    if (sqlite3_exec(db, sql, nullptr, nullptr, &errMsg) != SQLITE_OK) {
        std::cerr << "SQL error: " << errMsg << std::endl;
        sqlite3_free(errMsg);
    }
}

void insertStockOrder(sqlite3* db, const std::string& stockName, int quantity) {
    const char* sql = "INSERT INTO stock_orders (stock_name, quantity) VALUES (?, ?);";
    sqlite3_stmt* stmt;

    if (sqlite3_prepare_v2(db, sql, -1, &stmt, nullptr) == SQLITE_OK) {
        sqlite3_bind_text(stmt, 1, stockName.c_str(), -1, SQLITE_STATIC);
        sqlite3_bind_int(stmt, 2, quantity);
        if (sqlite3_step(stmt) != SQLITE_DONE) {
            std::cerr << "Execution failed: " << sqlite3_errmsg(db) << std::endl;
        }
        sqlite3_finalize(stmt);
    } else {
        std::cerr << "Preparation failed: " << sqlite3_errmsg(db) << std::endl;
    }
}

int main() {
    sqlite3* db;
    if (sqlite3_open("stocks.db", &db)) {
        std::cerr << "Can't open database: " << sqlite3_errmsg(db) << std::endl;
        return 1;
    }

    createTableIfNotExists(db);

    crow::SimpleApp app;

    // Route to display the form
    CROW_ROUTE(app, "/")([] {
        return R"(
            <form action="/buy_order" method="post">
                Stock Name: <input type="text" name="stock_name"><br>
                Quantity: <input type="number" name="quantity"><br>
                <input type="submit" value="Buy">
            </form>
        )";
    });

    // Route to handle buy orders
    CROW_ROUTE(app, "/buy_order").methods("POST"_method)([db](const crow::request& req) {
        auto stockName = req.body; // Parse the body to get parameters
        auto quantity = req.body; // Parse the body to get parameters
        size_t pos = stockName.find('&');
        if (pos != std::string::npos) {
            stockName = stockName.substr(stockName.find('=') + 1, pos - stockName.find('=') - 1);
            quantity = std::stoi(stockName.substr(pos + 9)); // Adjust as necessary
        }

        insertStockOrder(db, stockName, quantity);
        return crow::response(302, "Stock order placed!<br><a href='/'>Go back</a>");
    });

    app.port(18080).multithreaded().run();

    sqlite3_close(db);
    return 0;
}
