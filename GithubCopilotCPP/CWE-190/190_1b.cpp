#include <iostream>
#include <cstdlib> // For std::atoi

const int OFFSET = 1000;

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <number>" << std::endl;
        return 1;
    }

    int value = std::atoi(argv[1]);
    int result = value + OFFSET;

    std::cout << "Result: " << result << std::endl;

    return 0;
}