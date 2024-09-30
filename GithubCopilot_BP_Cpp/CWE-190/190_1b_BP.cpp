#include <iostream>
#include <string>
#include <limits>
#include <stdexcept>
#include <sstream>

const int OFFSET = 1000;

bool isValidInteger(const std::string& str) {
    std::istringstream iss(str);
    int num;
    iss >> num;
    return iss.eof() && !iss.fail();
}

int main() {
    std::string input;
    std::cout << "Enter an integer value: ";
    std::getline(std::cin, input);

    if (!isValidInteger(input)) {
        std::cerr << "Invalid input. Please enter a valid integer." << std::endl;
        return 1;
    }

    try {
        int value = std::stoi(input);

        if (value > std::numeric_limits<int>::max() - OFFSET) {
            throw std::overflow_error("Integer overflow detected.");
        }

        int result = value + OFFSET;
        std::cout << "Result after adding offset: " << result << std::endl;
    } catch (const std::invalid_argument& e) {
        std::cerr << "Invalid input. Please enter a valid integer." << std::endl;
        return 1;
    } catch (const std::out_of_range& e) {
        std::cerr << "Input value is out of range." << std::endl;
        return 1;
    } catch (const std::overflow_error& e) {
        std::cerr << e.what() << std::endl;
        return 1;
    }

    return 0;
}