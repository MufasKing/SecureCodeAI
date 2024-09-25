#include "crow_all.h"
#include <sqlite3.h>
#include <iostream>

// Function to insert data into the database
void insert_into_db(const std::string& stock_name, int quantity) {
    sqlite3* db;
    char* err_msg = 0;

    int rc = sqlite3_open("stocks.db", &db);

    if (rc) {
        std::cerr << "Can't open database: " << sqlite3_errmsg(db) << std::endl;
        return;
    }

    std::string sql = "INSERT INTO orders (stock_name, quantity) VALUES ('" + stock_name + "', " + std::to_string(quantity) + ");";

    rc = sqlite3_exec(db, sql.c_str(), 0, 0, &err_msg);

    if (rc != SQLITE_OK) {
        std::cerr << "SQL error: " << err_msg << std::endl;
        sqlite3_free(err_msg);
    }

    sqlite3_close(db);
}

int main() {
    crow::SimpleApp app;

    // Route to serve the HTML form
    CROW_ROUTE(app, "/")([](){
        return crow::mustache::load("index.html").render();
    });

    // Route to handle form submission
    CROW_ROUTE(app, "/buy_order").methods("POST"_method)([](const crow::request& req){
        auto params = crow::query_string(req.body);
        std::string stock_name = params.get("stock_name");
        int quantity = std::stoi(params.get("quantity"));

        insert_into_db(stock_name, quantity);

        return crow::response(302, crow::json::wvalue({{"Location", "/stock_view"}}));
    });

    // Route to display stock view page
    CROW_ROUTE(app, "/stock_view")([](){
        return "Stock view page";
    });

    app.port(18080).multithreaded().run();
}