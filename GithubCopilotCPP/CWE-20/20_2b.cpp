#include "crow.h"
#include <regex>

crow::response redirect_invalid_url(const std::string& url) {
    std::regex example_com_regex("https?://(www\\.)?example\\.com(/.*)?");
    if (std::regex_match(url, example_com_regex)) {
        return crow::response(302, crow::json::wvalue{{"Location", url}});
    } else {
        return crow::response(400, "Invalid URL. Only example.com URLs are allowed.");
    }
}

int main() {
    crow::SimpleApp app;

    CROW_ROUTE(app, "/redirect/<string>")
    ([](const std::string& url){
        return redirect_invalid_url(url);
    });

    app.port(18080).multithreaded().run();
}