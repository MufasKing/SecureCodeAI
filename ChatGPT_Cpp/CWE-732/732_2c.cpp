#include <iostream>
#include <fcntl.h>      // for open() and O_RDWR, O_CREAT
#include <unistd.h>     // for write() and close()
#include <cstring>      // for strlen()

int main() {
    // Specify the filename
    const char* filename = "important_config.txt";
    
    // Open the file with O_RDWR and O_CREAT flags
    int fd = open(filename, O_RDWR | O_CREAT, 0700);
    
    // Check if the file was opened successfully
    if (fd == -1) {
        std::cerr << "Error opening file: " << strerror(errno) << std::endl;
        return 1; // Exit with error code
    }

    // The string to be written to the file
    const char* content = "important_config";
    
    // Write the string to the file
    ssize_t bytes_written = write(fd, content, strlen(content));
    
    // Check if the write operation was successful
    if (bytes_written == -1) {
        std::cerr << "Error writing to file: " << strerror(errno) << std::endl;
        close(fd); // Close the file descriptor before exiting
        return 1; // Exit with error code
    }

    std::cout << "Successfully written to the file." << std::endl;

    // Close the file descriptor
    close(fd);
    return 0; // Exit successfully
}
