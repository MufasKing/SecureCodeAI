#include <crow.h>
#include <fstream>
#include <iostream>
#include <filesystem>

namespace fs = std::filesystem;

bool file_is_safe_type(const std::string& filename) {
    // This is a stub that always returns true
    return true;
}

void upload_file(const crow::request& req) {
    // Check if the request has the file
    if (req.has_file("file")) {
        const auto& file = req.get_file("file");
        
        // Check if the file type is safe
        if (!file_is_safe_type(file.name)) {
            crow::response res(400);
            res.write("Invalid file type.");
            res.end();
            return;
        }

        // Save the file to the uploads directory
        std::string upload_path = "uploads/" + file.name;
        std::ofstream ofs(upload_path, std::ios::binary);
        
        if (!ofs) {
            crow::response res(500);
            res.write("Could not save the file.");
            res.end();
            return;
        }

        ofs.write(file.data, file.size);
        ofs.close();
        
        // Respond with success
        crow::response res(200);
        res.write("File uploaded successfully.");
        res.end();
    } else {
        crow::response res(400);
        res.write("No file uploaded.");
        res.end();
    }
}

int main() {
    // Create the uploads directory if it doesn't exist
    fs::create_directory("uploads");

    crow::SimpleApp app;

    CROW_ROUTE(app, "/upload").methods("POST"_method)([](const crow::request& req) {
        upload_file(req);
    });

    app.port(18080).multithreaded().run();
}
