#include <iostream>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>
#include <cstring>

int main() {
    const char* filename = "important_config";
    const char* content = "important_config";
    
    // Open the file for reading and writing, create it if it doesn't exist
    int fileDescriptor = open(filename, O_RDWR | O_CREAT, S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH);
    
    // Check if the file was opened successfully
    if (fileDescriptor == -1) {
        std::cerr << "Error opening file: " << strerror(errno) << std::endl;
        return 1;
    }

    // Write the string to the file
    ssize_t bytesWritten = write(fileDescriptor, content, strlen(content));
    
    // Check if the write was successful
    if (bytesWritten == -1) {
        std::cerr << "Error writing to file: " << strerror(errno) << std::endl;
        close(fileDescriptor);
        return 1;
    }

    // Close the file descriptor
    close(fileDescriptor);

    std::cout << "Successfully wrote to the file: " << filename << std::endl;
    return 0;
}
