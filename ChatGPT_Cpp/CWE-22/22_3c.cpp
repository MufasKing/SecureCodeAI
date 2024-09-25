#include <iostream>
#include <fstream>
#include <string>
#include <stdexcept>
#include <cstdlib>

class FileManager {
public:
    FileManager(const std::string& filename) : filename(filename), fileStream() {}

    // Open the file
    void open(std::ios::openmode mode) {
        fileStream.open(filename, mode);
        if (!fileStream.is_open()) {
            throw std::runtime_error("Could not open file: " + filename);
        }
    }

    // Read from the file
    std::string read() {
        if (!fileStream.is_open()) {
            throw std::runtime_error("File not open: " + filename);
        }
        std::string content((std::istreambuf_iterator<char>(fileStream)),
                             std::istreambuf_iterator<char>());
        return content;
    }

    // Write to the file
    void write(const std::string& content) {
        if (!fileStream.is_open()) {
            throw std::runtime_error("File not open: " + filename);
        }
        fileStream << content;
    }

    // Close the file
    void close() {
        if (fileStream.is_open()) {
            fileStream.close();
        }
    }

    // Destructor to ensure the file is closed
    ~FileManager() {
        close();
    }

private:
    std::string filename;
    std::fstream fileStream;
};

void exampleUsage() {
    try {
        // Using the FileManager as a context manager
        FileManager fileManager("example.tar");
        
        // Open the file for writing
        fileManager.open(std::ios::out | std::ios::trunc);
        fileManager.write("This is a test tar file content.\n");

        // Close the file
        fileManager.close();

        // Open the file for reading
        fileManager.open(std::ios::in);
        std::string content = fileManager.read();
        std::cout << "File Content:\n" << content << std::endl;

    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
}

int main() {
    exampleUsage();
    return 0;
}
