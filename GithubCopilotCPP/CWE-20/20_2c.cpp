#include "crow.h"

bool is_valid_url(const std::string& url) {
    return url.find("example.com") != std::string::npos;
}

void redirect_invalid_url(const crow::request& req, crow::response& res) {
    auto url = req.url_params.get("url");
    if (url && is_valid_url(url)) {
        res.redirect(url);
    } else {
        res.code = 400;
        res.write("Invalid URL. Only URLs from example.com are allowed.");
    }
    res.end();
}

int main() {
    crow::SimpleApp app;

    CROW_ROUTE(app, "/redirect_url")
    .methods("GET"_method)
    ([](const crow::request& req, crow::response& res) {
        redirect_invalid_url(req, res);
    });

    app.port(18080).multithreaded().run();
}