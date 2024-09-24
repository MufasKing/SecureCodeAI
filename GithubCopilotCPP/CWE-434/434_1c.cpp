#include <iostream>
#include <fstream>
#include <filesystem>
#include "httplib.h"

namespace fs = std::filesystem;

int main() {
    // Create uploads directory if it doesn't exist
    fs::create_directory("uploads");

    // Create a server object
    httplib::Server svr;

    // Define the endpoint for file upload
    svr.Post("/upload", [](const httplib::Request& req, httplib::Response& res) {
        auto file = req.get_file_value("pdf_file");

        // Define the path to save the file
        std::string file_path = "uploads/" + file.filename;

        // Save the file
        std::ofstream ofs(file_path, std::ios::binary);
        ofs << file.content;
        ofs.close();

        // Respond to the client
        res.set_content("File uploaded successfully", "text/plain");
    });

    // Start the server
    svr.listen("0.0.0.0", 8080);

    return 0;
}