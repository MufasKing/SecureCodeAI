#include <iostream>
#include <fstream>
#include <vector>
#include <numeric>

// Function to calculate checksum
unsigned int calculateChecksum(const std::vector<char>& buffer) {
    return std::accumulate(buffer.begin(), buffer.end(), 0u);
}

int main() {
    const std::string inputFileName = "input.txt";
    const std::string outputFileName = "output.txt";

    // Open the input file
    std::ifstream inputFile(inputFileName, std::ios::binary);
    if (!inputFile) {
        std::cerr << "Error opening input file: " << inputFileName << std::endl;
        return 1;
    }

    // Read the contents of the file into a buffer
    std::vector<char> buffer((std::istreambuf_iterator<char>(inputFile)), std::istreambuf_iterator<char>());
    inputFile.close();

    // Calculate the checksum
    unsigned int checksum = calculateChecksum(buffer);

    // Check if the buffer is empty
    if (checksum == 0) {
        std::cout << "The buffer is empty." << std::endl;
    }

    // Open the output file
    std::ofstream outputFile(outputFileName);
    if (!outputFile) {
        std::cerr << "Error opening output file: " << outputFileName << std::endl;
        return 1;
    }

    // Write the number of bytes read and the checksum to the output file
    outputFile << "Number of bytes read: " << buffer.size() << std::endl;
    outputFile << "Checksum: " << checksum << std::endl;
    outputFile.close();

    return 0;
}