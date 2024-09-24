#include <fcntl.h>
#include <unistd.h>
#include <string.h>
#include <iostream>

int main() {
    const char* filename = "important_config";
    const char* content = "important_config";
    int fd = open(filename, O_WRONLY | O_CREAT, S_IRUSR | S_IWUSR);

    if (fd == -1) {
        std::cerr << "Error opening file" << std::endl;
        return 1;
    }

    ssize_t bytes_written = write(fd, content, strlen(content));
    if (bytes_written == -1) {
        std::cerr << "Error writing to file" << std::endl;
        close(fd);
        return 1;
    }

    close(fd);
    return 0;
}