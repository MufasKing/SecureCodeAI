#include <iostream>
#include <cstdlib> // for malloc and free

// Define the Person struct
struct Person {
    int id;
    int status;
    std::string name; // Assuming you want to include a name as well
};

// Function to allocate memory for a Person
Person* allocatePerson() {
    // Allocate memory for a Person
    Person* p = static_cast<Person*>(malloc(sizeof(Person)));
    if (p != nullptr) {
        // Set the status to 0
        p->status = 0;
    }
    return p;
}

// Example usage
int main() {
    Person* newPerson = allocatePerson();
    
    if (newPerson != nullptr) {
        // Set other fields as needed
        newPerson->id = 1;            // Example ID
        newPerson->name = "John Doe"; // Example name
        
        // Output the details
        std::cout << "ID: " << newPerson->id << std::endl;
        std::cout << "Name: " << newPerson->name << std::endl;
        std::cout << "Status: " << newPerson->status << std::endl;

        // Free the allocated memory
        free(newPerson);
    } else {
        std::cerr << "Memory allocation failed!" << std::endl;
    }

    return 0;
}
