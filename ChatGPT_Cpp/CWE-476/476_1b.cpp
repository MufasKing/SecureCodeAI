#include <iostream>
#include <cstdlib> // for malloc and free

struct person {
    int id;
    char name[50];
    int status; // Assuming status is an integer
};

// Function to allocate memory for a person
person* allocatePerson() {
    // Allocate memory for one person
    person* p = (person*)malloc(sizeof(person)); // Cast to person* for good practice
    if (p == nullptr) {
        std::cerr << "Memory allocation failed" << std::endl;
        return nullptr; // Return nullptr if allocation fails
    }
    
    // Initialize the status field
    p->status = 0;

    return p; // Return the pointer to the allocated memory
}

// Example usage
int main() {
    person* newPerson = allocatePerson();
    
    if (newPerson != nullptr) {
        std::cout << "Person allocated with status: " << newPerson->status << std::endl;
        
        // Don't forget to free the allocated memory
        free(newPerson);
    }

    return 0;
}
