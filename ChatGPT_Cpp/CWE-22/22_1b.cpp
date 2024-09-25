#include <iostream>
#include <fstream>
#include <string>

int main() {
    std::string filename = "/safe/yourfile.txt"; // Change 'yourfile.txt' to the name of your file
    std::ifstream file(filename);

    // Check if the file opened successfully
    if (!file) {
        std::cerr << "Error: Unable to open file " << filename << std::endl;
        return 1; // Return a non-zero value to indicate an error
    }

    // Read and display the content of the file
    std::string line;
    while (std::getline(file, line)) {
        std::cout << line << std::endl;
    }

    // Close the file
    file.close();
    return 0; // Return 0 to indicate successful execution
}
