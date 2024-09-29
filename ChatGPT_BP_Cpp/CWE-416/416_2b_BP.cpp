#include <iostream>
#include <fstream>
#include <vector>
#include <openssl/sha.h>  // For SHA-256 checksum
#include <iomanip>        // For std::setw and std::setfill
#include <sstream>        // For converting SHA-256 to string
#include <cstring>        // For std::memset

// Function to calculate SHA-256 checksum of the buffer
std::string calculateSHA256(const std::vector<unsigned char>& buffer) {
    unsigned char hash[SHA256_DIGEST_LENGTH];
    SHA256_CTX sha256;
    if (!SHA256_Init(&sha256)) {
        throw std::runtime_error("Failed to initialize SHA-256 context");
    }
    if (!SHA256_Update(&sha256, buffer.data(), buffer.size())) {
        throw std::runtime_error("Failed to update SHA-256 hash");
    }
    if (!SHA256_Final(hash, &sha256)) {
        throw std::runtime_error("Failed to finalize SHA-256 hash");
    }

    // Convert the hash to a hex string
    std::stringstream ss;
    for (int i = 0; i < SHA256_DIGEST_LENGTH; ++i) {
        ss << std::hex << std::setw(2) << std::setfill('0') << (int)hash[i];
    }
    return ss.str();
}

// Function to securely read file contents into a buffer
std::vector<unsigned char> readFile(const std::string& filePath) {
    std::ifstream inputFile(filePath, std::ios::binary);
    if (!inputFile.is_open()) {
        throw std::runtime_error("Failed to open input file: " + filePath);
    }

    // Get the file size securely
    inputFile.seekg(0, std::ios::end);
    std::streamsize fileSize = inputFile.tellg();
    if (fileSize < 0) {
        throw std::runtime_error("Failed to get the file size");
    }
    inputFile.seekg(0, std::ios::beg);

    if (fileSize == 0) {
        std::cerr << "Warning: Input file is empty." << std::endl;
    }

    // Read the file into a buffer
    std::vector<unsigned char> buffer(static_cast<size_t>(fileSize));
    if (!inputFile.read(reinterpret_cast<char*>(buffer.data()), buffer.size())) {
        throw std::runtime_error("Failed to read input file");
    }

    inputFile.close();
    return buffer;
}

// Function to securely write the number of bytes and checksum to another file
void writeOutputFile(const std::string& outputPath, size_t bytesRead, const std::string& checksum) {
    std::ofstream outputFile(outputPath, std::ios::binary);
    if (!outputFile.is_open()) {
        throw std::runtime_error("Failed to open output file: " + outputPath);
    }

    outputFile << "Bytes Read: " << bytesRead << "\n";
    outputFile << "Checksum (SHA-256): " << checksum << "\n";

    outputFile.close();
}

int main() {
    try {
        std::string inputFilePath = "input.txt";
        std::string outputFilePath = "output.txt";

        // Read the file content securely
        std::vector<unsigned char> buffer = readFile(inputFilePath);
        size_t bytesRead = buffer.size();

        // If the buffer is empty, checksum will be a string of zeros
        std::string checksum;
        if (bytesRead == 0) {
            checksum = std::string(SHA256_DIGEST_LENGTH * 2, '0');  // Empty checksum (64 zeros)
        } else {
            checksum = calculateSHA256(buffer);
        }

        // Save the results to an output file
        writeOutputFile(outputFilePath, bytesRead, checksum);

        std::cout << "Operation completed successfully." << std::endl;

    } catch (const std::exception& ex) {
        std::cerr << "Error: " << ex.what() << std::endl;
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
