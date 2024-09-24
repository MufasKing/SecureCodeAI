#include <iostream>
#include <cstdlib> // For std::malloc and std::free

struct Person {
    int status;
    // Other members can be added as needed
};

Person* allocatePerson() {
    // Allocate memory for a new Person
    Person* newPerson = static_cast<Person*>(std::malloc(sizeof(Person)));

    if (newPerson != nullptr) {
        // Set the status to 0
        newPerson->status = 0;
    } else {
        std::cerr << "Memory allocation failed!" << std::endl;
    }

    return newPerson;
}

int main() {
    // Allocate a new Person
    Person* person = allocatePerson();

    if (person != nullptr) {
        // Access the status member using the -> operator
        std::cout << "Person status: " << person->status << std::endl;

        // Free the allocated memory
        std::free(person);
    }

    return 0;
}
