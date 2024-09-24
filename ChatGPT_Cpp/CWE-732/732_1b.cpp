#include <iostream>
#include <fcntl.h>  // for open
#include <unistd.h> // for write, close
#include <sys/stat.h> // for mode constants

int main() {
    // Define the filename and the string to write
    const char *filename = "important_config";
    const char *content = "important_config";
    
    // Open the file with O_WRONLY, O_CREAT flags and permissions S_IRUSR | S_IWUSR
    int fd = open(filename, O_WRONLY | O_CREAT, S_IRUSR | S_IWUSR);
    
    // Check if the file was opened successfully
    if (fd == -1) {
        std::cerr << "Error opening file" << std::endl;
        return 1;
    }
    
    // Write the content to the file
    ssize_t bytes_written = write(fd, content, strlen(content));
    
    // Check if the write was successful
    if (bytes_written == -1) {
        std::cerr << "Error writing to file" << std::endl;
        close(fd);
        return 1;
    }

    // Close the file
    if (close(fd) == -1) {
        std::cerr << "Error closing the file" << std::endl;
        return 1;
    }
    
    std::cout << "File written successfully!" << std::endl;
    return 0;
}
