#include <iostream>
#include <fstream>
#include <vector>
#include <cstdint>
#include <cstring>
#include <stdexcept>
#include <iomanip> // For std::setw and std::setfill

// Function to calculate checksum (simple sum of bytes modulo 256)
uint8_t calculateChecksum(const std::vector<uint8_t>& buffer) {
    uint32_t checksum = 0;
    for (uint8_t byte : buffer) {
        checksum += byte;
    }
    return static_cast<uint8_t>(checksum % 256);
}

// Function to read file into buffer
std::vector<uint8_t> readFileIntoBuffer(const std::string& filename) {
    // Open the file in binary mode
    std::ifstream inputFile(filename, std::ios::binary);
    if (!inputFile) {
        throw std::runtime_error("Error: Could not open file for reading.");
    }

    // Seek to the end to get file size
    inputFile.seekg(0, std::ios::end);
    std::streampos fileSize = inputFile.tellg();
    if (fileSize <= 0) {
        throw std::runtime_error("Error: File is empty or unreadable.");
    }

    // Resize buffer to file size
    std::vector<uint8_t> buffer(fileSize);

    // Seek back to the beginning and read the file into buffer
    inputFile.seekg(0, std::ios::beg);
    inputFile.read(reinterpret_cast<char*>(buffer.data()), buffer.size());

    if (!inputFile) {
        throw std::runtime_error("Error: Failed to read the entire file.");
    }

    inputFile.close();
    return buffer;
}

// Function to save checksum and bytes read to output file
void saveResultsToFile(const std::string& outputFilename, size_t bytesRead, uint8_t checksum) {
    std::ofstream outputFile(outputFilename, std::ios::out | std::ios::trunc);
    if (!outputFile) {
        throw std::runtime_error("Error: Could not open file for writing.");
    }

    // Output number of bytes read and checksum in a secure format
    outputFile << "Bytes Read: " << bytesRead << "\n";
    outputFile << "Checksum: " << std::setw(2) << std::setfill('0') << std::hex << static_cast<int>(checksum) << "\n";

    if (!outputFile) {
        throw std::runtime_error("Error: Failed to write to output file.");
    }

    outputFile.close();
}

int main(int argc, char* argv[]) {
    if (argc != 3) {
        std::cerr << "Usage: " << argv[0] << " <input_file> <output_file>" << std::endl;
        return 1;
    }

    std::string inputFilename = argv[1];
    std::string outputFilename = argv[2];

    try {
        // Read file into buffer
        std::vector<uint8_t> buffer = readFileIntoBuffer(inputFilename);

        // Calculate checksum
        uint8_t checksum = calculateChecksum(buffer);

        // If checksum is 0, buffer is considered empty
        if (checksum == 0) {
            std::cerr << "Warning: Checksum is 0. Buffer may be empty or only contain null bytes." << std::endl;
        }

        // Save results to the output file
        saveResultsToFile(outputFilename, buffer.size(), checksum);

        std::cout << "Processing complete. Results saved to " << outputFilename << std::endl;
    }
    catch (const std::exception& e) {
        std::cerr << e.what() << std::endl;
        return 1;
    }

    return 0;
}
