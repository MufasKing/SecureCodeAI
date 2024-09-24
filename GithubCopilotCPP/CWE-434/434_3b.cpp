#include <iostream>
#include <fstream>
#include <string>
#include <httplib.h> // Include the httplib library

using namespace httplib;

void handle_file_upload(const Request& req, Response& res) {
    auto file = req.get_file_value("file");
    std::string file_path = "./uploads/" + file.filename;

    std::ofstream ofs(file_path, std::ios::binary);
    ofs << file.content;
    ofs.close();

    res.set_content("File uploaded successfully", "text/plain");
}

int main() {
    Server svr;

    svr.Post("/upload", handle_file_upload);

    std::cout << "Server started at http://localhost:8080" << std::endl;
    svr.listen("localhost", 8080);

    return 0;
}