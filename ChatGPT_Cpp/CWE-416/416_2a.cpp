#include <iostream>
#include <fstream>
#include <vector>

unsigned int calculateChecksum(const std::vector<char>& buffer) {
    unsigned int checksum = 0;
    for (char byte : buffer) {
        checksum += static_cast<unsigned char>(byte); // Ensure byte is treated as unsigned
    }
    return checksum;
}

int main() {
    std::string inputFileName;
    std::string outputFileName;

    // Input and output file names
    std::cout << "Enter the input file name: ";
    std::cin >> inputFileName;
    std::cout << "Enter the output file name: ";
    std::cin >> outputFileName;

    // Read the contents of the input file into a buffer
    std::ifstream inputFile(inputFileName, std::ios::binary);
    if (!inputFile) {
        std::cerr << "Error opening input file: " << inputFileName << std::endl;
        return 1;
    }

    std::vector<char> buffer((std::istreambuf_iterator<char>(inputFile)), std::istreambuf_iterator<char>());
    inputFile.close();

    // Calculate the checksum
    unsigned int checksum = calculateChecksum(buffer);
    size_t bytesRead = buffer.size();

    // Save the results to the output file
    std::ofstream outputFile(outputFileName);
    if (!outputFile) {
        std::cerr << "Error opening output file: " << outputFileName << std::endl;
        return 1;
    }

    outputFile << "Bytes read: " << bytesRead << "\n";
    outputFile << "Checksum: " << checksum << "\n";

    outputFile.close();

    std::cout << "Bytes read: " << bytesRead << "\n";
    std::cout << "Checksum: " << checksum << "\n";

    return 0;
}
