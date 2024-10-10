#include <iostream>
#include <fstream>
#include <string>
#include <filesystem>
#include <cpprest/http_listener.h>
#include <cpprest/uri.h>
#include <cpprest/json.h>

using namespace web;
using namespace web::http;
using namespace web::http::experimental::listener;
using namespace std;
namespace fs = std::filesystem;

void handle_get(http_request request) {
    auto paths = uri::split_path(uri::decode(request.relative_uri().path()));
    if (paths.size() != 1) {
        request.reply(status_codes::BadRequest, U("Invalid request"));
        return;
    }

    string file_name = paths[0];
    string file_path = "images/" + file_name;

    if (fs::exists(file_path)) {
        ifstream file(file_path, ios::in | ios::binary);
        if (file) {
            ostringstream contents;
            contents << file.rdbuf();
            file.close();
            request.reply(status_codes::OK, contents.str(), U("application/octet-stream"));
        } else {
            request.reply(status_codes::InternalError, U("Could not read file"));
        }
    } else {
        request.reply(status_codes::NotFound, U("File not found"));
    }
}

int main() {
    http_listener listener(U("http://localhost:8080"));

    listener.support(methods::GET, handle_get);

    try {
        listener
            .open()
            .then([&listener]() { cout << "Starting to listen at: " << listener.uri().to_string() << endl; })
            .wait();

        while (true);
    } catch (const exception& e) {
        cerr << "Error: " << e.what() << endl;
    }

    return 0;
}