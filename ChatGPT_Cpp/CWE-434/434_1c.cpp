#include <cpprest/http_listener.h>
#include <cpprest/uri.h>
#include <cpprest/streambuf.h>
#include <cpprest/http_client.h>
#include <cpprest/uri.h>
#include <cpprest/filestream.h>
#include <cpprest/producerconsumerstream.h>
#include <iostream>
#include <fstream>

using namespace web;
using namespace web::http;
using namespace web::http::experimental::listener;

const std::string UPLOAD_FOLDER = "uploads/";

void handle_post(http_request request) {
    request.extract_vector().then([=](std::vector<unsigned char> body) {
        std::string file_path = UPLOAD_FOLDER + "uploaded_file.pdf";

        // Ensure the upload directory exists
        std::filesystem::create_directories(UPLOAD_FOLDER);

        // Write the file
        std::ofstream file(file_path, std::ios::binary);
        if (file.is_open()) {
            file.write(reinterpret_cast<const char*>(body.data()), body.size());
            file.close();
            request.reply(status_codes::OK, U("File uploaded successfully."));
        } else {
            request.reply(status_codes::InternalError, U("Failed to open file for writing."));
        }
    }).wait();
}

int main() {
    uri_builder uri(U("http://localhost:8080/upload"));
    auto addr = uri.to_uri().to_string();
    listener l(addr);

    l.support(methods::POST, handle_post);

    try {
        l
            .open()
            .then([&l](){ std::wcout << L"Starting to listen at: " << l.uri().to_string() << std::endl; })
            .wait();

        std::string line;
        std::getline(std::cin, line);
    } catch (const std::exception& e) {
        std::cerr << "An error occurred: " << e.what() << std::endl;
    }

    return 0;
}
