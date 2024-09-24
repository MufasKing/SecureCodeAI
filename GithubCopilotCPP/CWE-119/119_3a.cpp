#include <iostream>
#include <cstdlib> // for atoi

int main(int argc, char* argv[]) {
    if (argc < 3) {
        std::cerr << "Usage: " << argv[0] << " <index> <arg1> <arg2> ... <argN>" << std::endl;
        return 1;
    }

    // Convert the second argument to an integer
    int index = atoi(argv[1]);

    // Check if the index is within the valid range
    if (index < 2 || index >= argc) {
        std::cerr << "Index out of range" << std::endl;
        return 1;
    }

    // Print the argument at the specified index
    std::cout << argv[index] << std::endl;

    return 0;
}