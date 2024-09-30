#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>

int main() {
    // Step 1: Memory Allocation (Buffer Size = 1024 bytes)
    size_t bufferSize = 1024;
    char* buf = (char*)malloc(bufferSize * sizeof(char));
    
    if (buf == nullptr) {
        std::cerr << "Memory allocation failed!" << std::endl;
        return 1; // Exit with error code if memory allocation fails
    }

    // Step 2: Input Handling (Reading 10 characters from stdin)
    std::cout << "Please enter up to 10 characters: ";

    // Step 3: Buffer Size Limit & Error Handling
    if (fgets(buf, 11, stdin) == nullptr) {
        std::cerr << "Error reading input!" << std::endl;
        free(buf); // Free memory in case of error
        return 1;
    }

    // Step 4: Input Validation & Null Termination
    // fgets ensures null-termination, but we can explicitly check and trim newlines.
    size_t inputLength = strlen(buf);
    if (inputLength > 0 && buf[inputLength - 1] == '\n') {
        buf[inputLength - 1] = '\0'; // Replace newline character with null-terminator
    }

    // Step 5: Output and Validation
    std::cout << "You entered: " << buf << std::endl;

    // Step 6: Memory Deallocation
    free(buf);

    return 0;
}
