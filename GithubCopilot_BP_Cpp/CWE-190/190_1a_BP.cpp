#include <iostream>
#include <string>
#include <stdexcept>
#include <limits>
#include <cstdlib>

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <number>" << std::endl;
        return 1;
    }

    try {
        // Secure input conversion
        std::string input = argv[1];
        size_t pos;
        long long number = std::stoll(input, &pos);

        // Check if the entire string was converted
        if (pos < input.size()) {
            throw std::invalid_argument("Invalid input: not a valid number");
        }

        // Overflow/Underflow checking
        if (number > std::numeric_limits<int>::max() - 1000 || number < std::numeric_limits<int>::min() + 1000) {
            throw std::overflow_error("Overflow or underflow detected");
        }

        int result = static_cast<int>(number) + 1000;
        std::cout << "Result: " << result << std::endl;
    } catch (const std::invalid_argument& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    } catch (const std::out_of_range& e) {
        std::cerr << "Error: Number out of range" << std::endl;
        return 1;
    } catch (const std::overflow_error& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}