#include <cstdlib>
#include <iostream>

int main() {
    // Define the command to unzip the archive
    const char* command = "unzip archive.zip -d /tmp/unpack";
    
    // Execute the command
    int result = system(command);
    
    // Check if the command was successful
    if (result == 0) {
        std::cout << "Files successfully unzipped to /tmp/unpack" << std::endl;
    } else {
        std::cerr << "Failed to unzip files" << std::endl;
    }
    
    return result;
}