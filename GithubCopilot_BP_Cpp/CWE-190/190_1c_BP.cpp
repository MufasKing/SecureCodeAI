#include <iostream>
#include <string>
#include <stdexcept>
#include <memory>

int readAndValidateInput(const std::string& input) {
    try {
        size_t pos;
        int value = std::stoi(input, &pos);
        if (pos < input.size()) {
            throw std::invalid_argument("Trailing characters after number");
        }
        return value;
    } catch (const std::invalid_argument& e) {
        throw std::runtime_error("Invalid input: not a valid integer");
    } catch (const std::out_of_range& e) {
        throw std::runtime_error("Invalid input: integer out of range");
    }
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <integer>" << std::endl;
        return 1;
    }

    try {
        const std::string input(argv[1]);
        int value = readAndValidateInput(input);
        value += 1000;
        std::cout << "Result: " << value << std::endl;
    } catch (const std::runtime_error& e) {
        std::cerr << e.what() << std::endl;
        return 1;
    }

    return 0;
}