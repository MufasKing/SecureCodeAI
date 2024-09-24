#include <iostream>
#include <fstream>
#include <vector>

unsigned long calculateChecksum(const std::vector<char>& buffer) {
    unsigned long checksum = 0;
    for (char byte : buffer) {
        checksum += static_cast<unsigned char>(byte);
    }
    return checksum;
}

int main() {
    std::string inputFileName = "input.txt";    // Name of the file to read from
    std::string outputFileName = "output.txt";  // Name of the file to write to

    // Open the input file
    std::ifstream inputFile(inputFileName, std::ios::binary);
    if (!inputFile) {
        std::cerr << "Error opening input file: " << inputFileName << std::endl;
        return 1;
    }

    // Read the contents of the file into a buffer
    std::vector<char> buffer((std::istreambuf_iterator<char>(inputFile)), std::istreambuf_iterator<char>());
    inputFile.close();

    // Calculate the checksum of the buffer
    unsigned long checksum = calculateChecksum(buffer);
    size_t bytesRead = buffer.size();

    // Open the output file
    std::ofstream outputFile(outputFileName);
    if (!outputFile) {
        std::cerr << "Error opening output file: " << outputFileName << std::endl;
        return 1;
    }

    // Write the number of bytes read and the checksum to the output file
    outputFile << "Bytes read: " << bytesRead << std::endl;
    outputFile << "Checksum: " << checksum << std::endl;

    outputFile.close();

    // Check if the checksum is zero (buffer is empty)
    if (checksum == 0) {
        std::cout << "The buffer is empty." << std::endl;
    } else {
        std::cout << "Bytes read: " << bytesRead << ", Checksum: " << checksum << std::endl;
    }

    return 0;
}
