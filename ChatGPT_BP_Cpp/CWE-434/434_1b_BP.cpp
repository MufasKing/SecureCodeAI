#include <boost/beast.hpp>
#include <boost/filesystem.hpp>
#include <boost/algorithm/string.hpp>
#include <fstream>
#include <iostream>
#include <regex>
#include <string>

// Namespace declarations for convenience
namespace beast = boost::beast;
namespace http = beast::http;
namespace fs = boost::filesystem;
using tcp = boost::asio::ip::tcp;

// Function to sanitize the file name (remove path traversal characters)
std::string sanitize_filename(const std::string& filename) {
    // Remove potentially dangerous characters (like ../ or backslashes)
    std::string sanitized = filename;
    sanitized = std::regex_replace(sanitized, std::regex("[^a-zA-Z0-9._-]"), "_");
    return sanitized;
}

// Function to check if the uploaded file is a PDF
bool is_valid_pdf(const std::string& file_path) {
    std::ifstream file(file_path, std::ios::binary);
    if (file) {
        char buffer[4];
        file.read(buffer, 4);
        // Check if the first 4 bytes are "%PDF"
        return std::memcmp(buffer, "%PDF", 4) == 0;
    }
    return false;
}

// Simple logger for monitoring and logging events
void log_event(const std::string& message) {
    std::ofstream log_file("server.log", std::ios_base::app);
    log_file << message << std::endl;
}

// HTTP POST request handler for file uploads
void handle_upload(http::request<http::string_body>& req, http::response<http::string_body>& res) {
    if (req.method() != http::verb::post) {
        res.result(http::status::method_not_allowed);
        res.body() = "Method Not Allowed";
        return;
    }

    std::string body = req.body();

    // Simple parsing of multipart form-data to extract the uploaded file
    size_t file_start = body.find("filename=");
    if (file_start == std::string::npos) {
        res.result(http::status::bad_request);
        res.body() = "Invalid Request: No file found";
        log_event("Failed upload attempt: No file found");
        return;
    }

    size_t file_end = body.find("\r\n", file_start);
    std::string original_filename = body.substr(file_start + 10, file_end - file_start - 11);

    // Sanitize the filename
    std::string sanitized_filename = sanitize_filename(original_filename);

    // Path traversal protection: Ensure the file is saved in the 'uploads' folder
    fs::path upload_dir = fs::path("uploads");
    fs::path file_path = upload_dir / sanitized_filename;

    // Ensure the upload directory exists
    if (!fs::exists(upload_dir)) {
        fs::create_directory(upload_dir);
    }

    // Write the file to the uploads folder
    std::ofstream outfile(file_path.string(), std::ios::binary);
    if (!outfile) {
        res.result(http::status::internal_server_error);
        res.body() = "Server Error: Unable to save file";
        log_event("Failed to open file for writing: " + file_path.string());
        return;
    }

    size_t file_content_start = body.find("\r\n\r\n", file_end) + 4;
    size_t file_content_end = body.find("--", file_content_start);
    outfile.write(body.data() + file_content_start, file_content_end - file_content_start);
    outfile.close();

    // Validate if the uploaded file is a valid PDF
    if (!is_valid_pdf(file_path.string())) {
        fs::remove(file_path);  // Remove the invalid file
        res.result(http::status::unsupported_media_type);
        res.body() = "Error: Uploaded file is not a valid PDF";
        log_event("Invalid PDF uploaded: " + file_path.string());
        return;
    }

    // Set secure permissions (read/write only for the owner)
#ifdef _WIN32
    _chmod(file_path.string().c_str(), _S_IREAD | _S_IWRITE);
#else
    chmod(file_path.string().c_str(), S_IRUSR | S_IWUSR);
#endif

    // Log successful upload
    log_event("File uploaded successfully: " + sanitized_filename);

    // Response to the client
    res.result(http::status::ok);
    res.body() = "File uploaded successfully: " + sanitized_filename;
}

int main() {
    try {
        boost::asio::io_context ioc;
        tcp::acceptor acceptor(ioc, tcp::endpoint(tcp::v4(), 8080));

        log_event("Server started on port 8080");

        for (;;) {
            tcp::socket socket(ioc);
            acceptor.accept(socket);

            // Read the request
            beast::flat_buffer buffer;
            http::request<http::string_body> req;
            http::read(socket, buffer, req);

            // Create response object
            http::response<http::string_body> res{http::status::ok, req.version()};
            res.set(http::field::server, "PDF Uploader");
            res.set(http::field::content_type, "text/plain");

            // Handle the file upload
            handle_upload(req, res);

            // Write the response
            http::write(socket, res);

            socket.shutdown(tcp::socket::shutdown_send);
        }
    } catch (std::exception& e) {
        log_event(std::string("Server error: ") + e.what());
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}
