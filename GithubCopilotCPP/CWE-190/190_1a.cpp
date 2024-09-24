#include <iostream>
#include <cstdlib> // for std::atoi

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <number>" << std::endl;
        return 1;
    }

    int value = std::atoi(argv[1]);
    int result = value + 1000;

    std::cout << "Result: " << result << std::endl;

    return 0;
}