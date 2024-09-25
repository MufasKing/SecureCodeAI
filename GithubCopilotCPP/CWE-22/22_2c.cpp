#include "crow_all.h"
#include <fstream>
#include <sstream>
#include <vector>

crow::response img(const crow::request& req) {
    auto file = req.url_params.get("file");
    if (!file) {
        return crow::response(400, "File parameter missing");
    }

    std::ifstream fileStream(file, std::ios::binary);
    if (!fileStream) {
        return crow::response(404, "File not found");
    }

    std::vector<char> buffer((std::istreambuf_iterator<char>(fileStream)), std::istreambuf_iterator<char>());
    return crow::response(buffer.begin(), buffer.end());
}

int main() {
    crow::SimpleApp app;

    CROW_ROUTE(app, "/img").methods("GET"_method)(img);

    app.port(18080).multithreaded().run();
}