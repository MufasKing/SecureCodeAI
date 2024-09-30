#include <iostream>
#include <fstream>
#include <filesystem>
#include <string>
#include <regex>

namespace fs = std::filesystem;

// Function to check if the file type is safe
bool file_is_safe_type(const std::string& filename) {
    // Define the allowed file types (you can add more)
    const std::regex allowed_file_types("(\\.jpg|\\.jpeg|\\.png|\\.gif|\\.pdf|\\.txt)$", std::regex::icase);

    // Check if the file matches one of the allowed types
    if (std::regex_search(filename, allowed_file_types)) {
        return true;
    }
    return false;
}

// Function to sanitize the filename by removing any dangerous characters
std::string sanitize_filename(const std::string& filename) {
    std::string sanitized_filename = filename;
    sanitized_filename = std::regex_replace(sanitized_filename, std::regex("[^a-zA-Z0-9._-]"), "_");
    return sanitized_filename;
}

// Function to handle the file upload
bool upload_file(const std::string& filepath) {
    try {
        // Check if the file exists
        if (!fs::exists(filepath)) {
            throw std::runtime_error("File does not exist.");
        }

        // Extract the filename from the filepath
        std::string filename = fs::path(filepath).filename().string();

        // Perform file type validation
        if (!file_is_safe_type(filename)) {
            throw std::runtime_error("File type is not allowed.");
        }

        // Sanitize the filename to prevent directory traversal attacks
        filename = sanitize_filename(filename);

        // Define the upload directory path
        const std::string upload_dir = "uploads";

        // Create the uploads directory if it does not exist
        if (!fs::exists(upload_dir)) {
            if (!fs::create_directory(upload_dir)) {
                throw std::runtime_error("Failed to create upload directory.");
            }
        }

        // Define the destination path for the uploaded file
        std::string destination = upload_dir + "/" + filename;

        // Perform secure file copy
        fs::copy_file(filepath, destination, fs::copy_options::overwrite_existing);

        std::cout << "File uploaded successfully to: " << destination << std::endl;
        return true;
    }
    catch (const std::exception& e) {
        // Error handling
        std::cerr << "Error: " << e.what() << std::endl;
        return false;
    }
}

int main() {
    std::string filepath;

    // Input validation: ensure the user inputs a valid filepath
    std::cout << "Enter the file path to upload: ";
    std::getline(std::cin, filepath);

    if (filepath.empty()) {
        std::cerr << "Error: File path cannot be empty." << std::endl;
        return 1;
    }

    // Attempt to upload the file
    if (!upload_file(filepath)) {
        std::cerr << "File upload failed." << std::endl;
        return 1;
    }

    return 0;
}
