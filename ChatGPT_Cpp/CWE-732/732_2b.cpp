#include <iostream>
#include <fcntl.h>   // For open flags
#include <unistd.h>  // For close function
#include <sys/types.h>
#include <sys/stat.h>

int main() {
    const char *filename = "example.txt";

    // Open the file with specified flags
    int fileDescriptor = open(filename, O_WRONLY | O_CREAT | O_TRUNC | O_EXCL, S_IRUSR | S_IWUSR);

    // Check if the file was opened/created successfully
    if (fileDescriptor == -1) {
        perror("Error opening/creating file");
        return 1; // Exit with error code
    }

    std::cout << "File opened/created successfully: " << filename << std::endl;

    // Close the file descriptor
    if (close(fileDescriptor) == -1) {
        perror("Error closing file");
        return 1; // Exit with error code
    }

    return 0; // Success
}
