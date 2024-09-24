#include "crow_all.h"
#include <fstream>
#include <filesystem>

int main() {
    crow::SimpleApp app;

    CROW_ROUTE(app, "/upload").methods("POST"_method)([](const crow::request& req) {
        auto file = req.get_file("pdf");
        if (file) {
            std::filesystem::create_directory("uploads");
            std::ofstream ofs("uploads/" + file->filename, std::ios::binary);
            ofs.write(file->body.data(), file->body.size());
            ofs.close();
            return crow::response(200, "File uploaded successfully.");
        } else {
            return crow::response(400, "File upload failed.");
        }
    });

    app.port(8080).multithreaded().run();
}