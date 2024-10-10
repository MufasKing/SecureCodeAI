#include <cstdlib>
#include <iostream>

int main() {
    // Command to unzip the archive.zip file to /tmp/unpack directory
    int result = system("unzip archive.zip -d /tmp/unpack");

    if (result == 0) {
        std::cout << "Extraction successful." << std::endl;
    } else {
        std::cerr << "Extraction failed." << std::endl;
    }

    return result;
}