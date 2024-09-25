#include <iostream>
#include <cstdlib> // for atoi()

int main(int argc, char* argv[]) {
    // Check if there are enough arguments passed
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <numbers> ..." << std::endl;
        return 1;
    }

    std::cout << "Program name: " << argv[0] << std::endl;

    for (int i = 1; i < argc; ++i) {
        int number = atoi(argv[i]);  // Convert string to int
        std::cout << "Argument " << i << " as integer: " << number << std::endl;
    }

    return 0;
}
