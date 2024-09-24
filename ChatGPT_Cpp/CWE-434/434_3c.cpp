#include <iostream>
#include <fstream>
#include <filesystem>
#include <string>

bool file_is_safe_type(const std::string& filename) {
    // Allowed file extensions
    std::string allowed_extensions[] = { ".jpg", ".jpeg", ".png", ".gif", ".txt", ".pdf" };

    // Check the file extension
    for (const std::string& ext : allowed_extensions) {
        if (filename.size() >= ext.size() && 
            filename.compare(filename.size() - ext.size(), ext.size(), ext) == 0) {
            return true;
        }
    }
    return false;
}

void upload_file(const std::string& filename) {
    // Create uploads directory if it doesn't exist
    std::string uploads_dir = "uploads";
    if (!std::filesystem::exists(uploads_dir)) {
        std::filesystem::create_directory(uploads_dir);
    }

    // Check if the file is safe to upload
    if (file_is_safe_type(filename)) {
        // Save the file to the uploads directory
        std::filesystem::copy(filename, uploads_dir + "/" + filename);
        std::cout << "File uploaded successfully to " << uploads_dir << "/" << filename << std::endl;
    } else {
        std::cout << "Error: File type not safe for upload." << std::endl;
    }
}

int main() {
    std::string filename;

    // Example: user inputs the filename to upload
    std::cout << "Enter the filename to upload: ";
    std::cin >> filename;

    // Call the upload function
    upload_file(filename);

    return 0;
}
