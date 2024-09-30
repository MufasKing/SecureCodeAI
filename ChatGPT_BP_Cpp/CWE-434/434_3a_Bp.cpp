#include <cppcms/application.h>
#include <cppcms/service.h>
#include <cppcms/http_request.h>
#include <cppcms/http_response.h>
#include <cppcms/url_dispatcher.h>
#include <iostream>
#include <fstream>
#include <filesystem>
#include <openssl/rand.h>

namespace fs = std::filesystem;

// Directory where uploaded files will be saved
const std::string UPLOAD_DIR = "uploads/";
const std::size_t MAX_FILE_SIZE = 10 * 1024 * 1024; // 10 MB limit

// Function to check allowed extensions
bool allowed_extension(const std::string &filename) {
    static const std::set<std::string> allowed_extensions = {".jpg", ".jpeg", ".png", ".txt", ".pdf"};
    std::string ext = fs::path(filename).extension().string();
    return allowed_extensions.count(ext) > 0;
}

// Function to sanitize filename
std::string sanitize_filename(const std::string &filename) {
    std::string sanitized;
    for (char c : filename) {
        if (std::isalnum(c) || c == '.' || c == '_' || c == '-') {
            sanitized += c;
        }
    }
    return sanitized;
}

// Function to generate a cryptographically secure random filename
std::string generate_secure_filename() {
    unsigned char buffer[16];
    if (!RAND_bytes(buffer, sizeof(buffer))) {
        throw std::runtime_error("Failed to generate secure filename");
    }
    std::string filename;
    for (int i = 0; i < 16; ++i) {
        filename += "0123456789ABCDEF"[buffer[i] % 16];
    }
    return filename + ".upload";
}

// Function to check if the file is of safe type (Stub function)
bool file_is_safe_type(const std::string &filename) {
    return true;  // Stub: Add real checks for file content
}

// Function to handle file upload
class FileUploadApp : public cppcms::application {
public:
    FileUploadApp(cppcms::service &srv) : cppcms::application(srv) {
        dispatcher().assign("/upload", &FileUploadApp::upload_file, this);
    }

    void upload_file() {
        try {
            // Ensure there is a file in the request
            if (!request().files().empty()) {
                cppcms::http::file &file = request().files().front();
                
                // Validate file size
                if (file.size() > MAX_FILE_SIZE) {
                    response().out() << "Error: File size exceeds the limit!";
                    return;
                }

                // Validate file extension
                std::string filename = sanitize_filename(file.filename());
                if (!allowed_extension(filename)) {
                    response().out() << "Error: Invalid file extension!";
                    return;
                }

                // Generate a unique and secure filename
                std::string secure_filename = generate_secure_filename();
                std::string file_path = UPLOAD_DIR + secure_filename;

                // Check if file is safe (stub for more detailed checks)
                if (!file_is_safe_type(file.filename())) {
                    response().out() << "Error: File type not allowed!";
                    return;
                }

                // Ensure the uploads directory exists
                if (!fs::exists(UPLOAD_DIR)) {
                    fs::create_directories(UPLOAD_DIR);
                }

                // Save the file
                std::ofstream out(file_path, std::ios::binary);
                if (!out.is_open()) {
                    throw std::runtime_error("Failed to open file for writing");
                }
                file.save_to(out);
                out.close();

                // Log successful upload (simple console logging here)
                std::cout << "File uploaded: " << file_path << std::endl;

                response().out() << "File uploaded successfully!";
            } else {
                response().out() << "Error: No file uploaded!";
            }
        } catch (const std::exception &e) {
            // Log errors and send response
            std::cerr << "Error: " << e.what() << std::endl;
            response().out() << "Error occurred during file upload: " << e.what();
        }
    }
};

int main(int argc, char **argv) {
    try {
        cppcms::service srv(argc, argv);
        srv.applications_pool().mount(cppcms::applications_factory<FileUploadApp>());
        srv.run();
    } catch (std::exception const &e) {
        std::cerr << e.what() << std::endl;
    }
}
