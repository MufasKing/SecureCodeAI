#include <iostream>
#include <cstdlib> // For atoi

int main(int argc, char* argv[]) {
    // Check if there are enough arguments
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <number>" << std::endl;
        return 1;
    }

    // Convert the second argument to an integer
    int number = atoi(argv[1]);

    // Output the converted number
    std::cout << "The converted number is: " << number << std::endl;

    return 0;
}