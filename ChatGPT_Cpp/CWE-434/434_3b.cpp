#include "crow.h"
#include <fstream>
#include <iostream>
#include <filesystem>

namespace fs = std::filesystem;

int main()
{
    crow::App app;

    // Define the upload directory
    const std::string upload_dir = "uploads";

    // Create the upload directory if it doesn't exist
    fs::create_directory(upload_dir);

    app.route_dynamic("/upload")
    ([&upload_dir](const crow::request& req) {
        if (req.method == "POST") {
            auto file = req.uploads.begin();
            if (file != req.uploads.end()) {
                const auto& upload_file = *file;
                // Save the uploaded file
                std::ofstream ofs(upload_dir + "/" + upload_file.filename, std::ios::binary);
                ofs.write(upload_file.body.data(), upload_file.body.size());
                ofs.close();
                return crow::response(200, "File uploaded successfully: " + upload_file.filename);
            }
            return crow::response(400, "No file uploaded.");
        }
        return crow::response(405, "Method Not Allowed");
    });

    app.route_dynamic("/")
    ([] {
        return R"(
            <html>
                <body>
                    <h1>File Upload</h1>
                    <form action="/upload" method="post" enctype="multipart/form-data">
                        <input type="file" name="file" />
                        <input type="submit" value="Upload" />
                    </form>
                </body>
            </html>
        )";
    });

    app.port(8080).multithreaded().run();
    return 0;
}
