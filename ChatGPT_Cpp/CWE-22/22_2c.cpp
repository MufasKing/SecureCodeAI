#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include "civetweb.h"

// Function to handle the /img route
int img_handler(struct mg_connection *conn, void *cbdata) {
    // Get the 'file' parameter from the query string
    const char *file_param = mg_get_query_string(conn);
    std::string file_name;

    // Parse the query string to get the file name
    if (file_param) {
        file_name = std::string(file_param);
    }

    // Open the file in binary mode
    std::ifstream file(file_name, std::ios::binary);
    if (!file.is_open()) {
        mg_send_http_error(conn, 404, "File not found");
        return 1; // Indicates an error
    }

    // Read the file's content into a string stream
    std::stringstream buffer;
    buffer << file.rdbuf();
    std::string content = buffer.str();

    // Send the file content as a response
    mg_send_header(conn, "Content-Type", "application/octet-stream");
    mg_send_header(conn, "Content-Length", std::to_string(content.size()).c_str());
    mg_write(conn, content.c_str(), content.size());

    return 1; // Indicates success
}

int main() {
    const char *options[] = {"listening_ports", "8080", nullptr};

    // Start the web server
    if (mg_start(NULL, 0, options) == NULL) {
        std::cerr << "Failed to start server!" << std::endl;
        return 1;
    }

    // Add the img handler for the /img route
    mg_set_request_handler("/img", img_handler, NULL);

    std::cout << "Server started on port 8080. Access /img?file=<your_file>." << std::endl;

    // Keep the server running
    for (;;) {
        // Wait for incoming connections
        mg_poll_server();
    }

    mg_stop(); // Clean up
    return 0;
}
