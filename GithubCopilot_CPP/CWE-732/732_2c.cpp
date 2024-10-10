#include <iostream>
#include <fcntl.h>
#include <unistd.h>
#include <cstring>

int main() {
    const char* filename = "config.txt";
    const char* content = "important_config";
    
    // Open the file with read/write permissions, create if it doesn't exist
    int fd = open(filename, O_RDWR | O_CREAT, 0700);
    if (fd == -1) {
        std::cerr << "Error opening file" << std::endl;
        return 1;
    }
    
    // Write the content to the file
    ssize_t bytes_written = write(fd, content, strlen(content));
    if (bytes_written == -1) {
        std::cerr << "Error writing to file" << std::endl;
        close(fd);
        return 1;
    }
    
    // Close the file descriptor
    close(fd);
    return 0;
}