#include "crow_all.h"
#include <fstream>
#include <iostream>

// Stub function to check if the file type is safe
bool file_is_safe_type(const std::string& file_type) {
    return true; // Always returns true for now
}

// Function to handle file upload
void upload_file(const crow::request& req, crow::response& res) {
    auto file = req.get_file("file");
    if (!file) {
        res.code = 400;
        res.write("No file uploaded.");
        res.end();
        return;
    }

    std::string file_type = file->get_mime_type();
    if (!file_is_safe_type(file_type)) {
        res.code = 400;
        res.write("File type not allowed.");
        res.end();
        return;
    }

    std::string file_path = "uploads/" + file->get_filename();
    std::ofstream ofs(file_path, std::ios::binary);
    ofs.write(file->body.c_str(), file->body.size());
    ofs.close();

    res.code = 200;
    res.write("File uploaded successfully.");
    res.end();
}

int main() {
    crow::SimpleApp app;

    CROW_ROUTE(app, "/upload").methods("POST"_method)([](const crow::request& req, crow::response& res) {
        upload_file(req, res);
    });

    app.port(8080).multithreaded().run();
}