#include <iostream>
#include <fcntl.h>   // for open() flags
#include <unistd.h>  // for close()
#include <sys/stat.h> // for file permissions

int main() {
    const char* filename = "important_config";

    // File permissions: owner can read (S_IRUSR) and write (S_IWUSR)
    mode_t permissions = S_IRUSR | S_IWUSR;

    // Flags: create if it doesn't exist, truncate if it does, write-only
    int flags = O_CREAT | O_TRUNC | O_WRONLY;

    // Open the file with specified flags and permissions
    int fd = open(filename, flags, permissions);

    if (fd == -1) {
        std::cerr << "Error: Could not open or create the file\n";
        return 1;
    }

    std::cout << "File created and opened successfully with appropriate permissions.\n";

    // Close the file descriptor
    close(fd);

    return 0;
}
