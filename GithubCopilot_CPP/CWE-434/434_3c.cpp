#include <iostream>
#include <fstream>
#include <filesystem>
#include <string>

// Function to check if the file is of a safe type
bool file_is_safe_type(const std::string& filename) {
    // Check the file extension
    std::string extension = filename.substr(filename.find_last_of(".") + 1);
    return (extension == "txt" || extension == "jpg" || extension == "png");
}

// Function to handle the upload of the file
bool upload_file(const std::string& filename) {
    if (!file_is_safe_type(filename)) {
        std::cerr << "File type is not safe to upload." << std::endl;
        return false;
    }

    // Create the uploads directory if it doesn't exist
    std::filesystem::path uploads_dir = std::filesystem::current_path() / "uploads";
    if (!std::filesystem::exists(uploads_dir)) {
        std::filesystem::create_directory(uploads_dir);
    }

    // Save the file to the uploads folder
    std::filesystem::path destination = uploads_dir / filename;
    std::ifstream src(filename, std::ios::binary);
    std::ofstream dst(destination, std::ios::binary);
    dst << src.rdbuf();

    std::cout << "File uploaded successfully to " << destination << std::endl;
    return true;
}

int main() {
    std::string filename = "example.txt"; // Replace with the actual file name
    upload_file(filename);
    return 0;
}