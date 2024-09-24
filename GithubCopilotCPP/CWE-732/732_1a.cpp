#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>
#include <iostream>

int main() {
    const char* filename = "important_config";
    int file_descriptor = open(filename, O_CREAT | O_TRUNC | O_WRONLY, S_IRUSR | S_IWUSR);

    if (file_descriptor == -1) {
        std::cerr << "Error creating or opening the file" << std::endl;
        return 1;
    }

    // File operations can be performed here

    if (close(file_descriptor) == -1) {
        std::cerr << "Error closing the file" << std::endl;
        return 1;
    }

    return 0;
}