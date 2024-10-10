#include <iostream>
#include <fcntl.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>

int main() {
    const char *filename = "example.txt";
    int fd = open(filename, O_WRONLY | O_CREAT | O_TRUNC | O_EXCL, S_IRUSR | S_IWUSR);

    if (fd == -1) {
        perror("Error opening file");
        return 1;
    }

    // File opened successfully, you can write to it here

    close(fd);
    return 0;
}