#include <iostream>
#include <cstdlib>  // For std::atoi

const int OFFSET = 1000;  // Constant offset

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <value>" << std::endl;
        return 1;
    }

    // Convert the command line argument to an integer
    int value = std::atoi(argv[1]);

    // Add the offset
    int result = value + OFFSET;

    // Output the result
    std::cout << "Original value: " << value << std::endl;
    std::cout << "Value after adding offset: " << result << std::endl;

    return 0;
}
