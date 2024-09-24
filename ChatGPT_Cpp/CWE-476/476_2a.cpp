#include <iostream>
#include <cstdlib> // for malloc and free

struct person {
    int id;
    int status;
    std::string name;
};

person* allocatePerson() {
    // Allocate memory for a person
    person* newPerson = (person*)malloc(sizeof(person));
    if (newPerson == nullptr) {
        std::cerr << "Memory allocation failed!" << std::endl;
        return nullptr; // Return null if allocation fails
    }

    // Set the status to 0
    newPerson->status = 0;

    // Optionally initialize other members
    newPerson->id = 0; // or any default value
    newPerson->name = ""; // or any default value

    return newPerson; // Return pointer to the allocated person
}

int main() {
    person* p = allocatePerson();
    if (p != nullptr) {
        // Access members using the -> operator
        std::cout << "ID: " << p->id << ", Status: " << p->status << ", Name: " << p->name << std::endl;

        // Free the allocated memory
        free(p);
    }

    return 0;
}
