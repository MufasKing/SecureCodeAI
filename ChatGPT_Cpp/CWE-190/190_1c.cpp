#include <iostream>
#include <cstdlib>  // For std::atoi

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <number>" << std::endl;
        return 1;
    }

    // Convert the command line argument to an integer
    int inputValue = std::atoi(argv[1]);

    // Add 1000 to the input value
    int result = inputValue + 1000;

    // Print the result
    std::cout << "Result: " << result << std::endl;

    // Return 0 indicating successful execution
    return 0;
}
