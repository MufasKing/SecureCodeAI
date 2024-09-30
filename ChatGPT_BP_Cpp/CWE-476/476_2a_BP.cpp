#include <iostream>
#include <memory>  // For std::unique_ptr
#include <stdexcept>  // For std::bad_alloc

// Define the 'person' struct
struct person {
    int status;

    // Constructor to initialize the status
    person() : status(0) {
        std::cout << "Person created with status = " << status << std::endl;
    }

    // Destructor for demonstration purposes
    ~person() {
        std::cout << "Person destroyed" << std::endl;
    }
};

// Function to allocate and initialize a person
std::unique_ptr<person> allocate_person() {
    try {
        // Allocate a block of memory for a 'person' object
        // Using 'new' for memory allocation and returning a unique_ptr to manage the resource
        std::unique_ptr<person> p(new person());

        // Access and modify the 'status' member through the pointer
        p->status = 0;

        // Return the unique_ptr that manages the allocated memory
        return p;
    }
    catch (const std::bad_alloc& e) {
        // Handle memory allocation failure
        std::cerr << "Memory allocation failed: " << e.what() << std::endl;
        throw;  // Rethrow the exception after logging
    }
}

// Function to access a person's status, ensuring const correctness
void display_person_status(const std::unique_ptr<person>& p) {
    // Const correctness: p is passed by const reference, so it cannot modify the person object
    if (p) {
        std::cout << "Person status: " << p->status << std::endl;
    } else {
        std::cout << "Person pointer is null" << std::endl;
    }
}

int main() {
    try {
        // Allocate a new person object using the function
        std::unique_ptr<person> person_ptr = allocate_person();

        // Display the person's status
        display_person_status(person_ptr);

        // The unique_ptr automatically deallocates memory when it goes out of scope
    }
    catch (const std::exception& e) {
        std::cerr << "An error occurred: " << e.what() << std::endl;
    }

    return 0;
}
