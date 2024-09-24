#include <iostream>
#include <cstdlib> // For std::atoi

int main(int argc, char* argv[]) {
    // Check if the user provided an argument
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <number>" << std::endl;
        return 1;
    }

    // Convert the input string to an integer
    int inputValue = std::atoi(argv[1]);

    // Add 1000 to the input value
    int result = inputValue + 1000;

    // Output the result
    std::cout << "Result: " << result << std::endl;

    return 0;
}
