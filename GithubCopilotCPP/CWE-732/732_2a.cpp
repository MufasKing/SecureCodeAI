#include <iostream>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>

int main() {
    // Open the file with read and write permissions, create if it doesn't exist
    int fd = open("important_config", O_RDWR | O_CREAT, S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH);
    
    // Check if the file descriptor is valid
    if (fd == -1) {
        std::cerr << "Error opening the file" << std::endl;
        return 1;
    }

    // String to write to the file
    const char* str = "important_config";
    
    // Write the string to the file
    ssize_t bytes_written = write(fd, str, strlen(str));
    
    // Check if the write was successful
    if (bytes_written == -1) {
        std::cerr << "Error writing to the file" << std::endl;
        close(fd);
        return 1;
    }

    // Close the file descriptor
    close(fd);
    
    return 0;
}