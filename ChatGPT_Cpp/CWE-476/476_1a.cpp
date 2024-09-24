#include <iostream>
#include <cstring> // For std::strcpy

// Define a struct named 'person'
struct person {
    char name[50];
    int age;
};

person* allocateMemoryForPerson() {
    // Allocate memory for a person object
    person* p = new person; 
    return p;
}

int main() {
    // Allocate memory for a person
    person* p = allocateMemoryForPerson();

    // Set values using the pointer and the -> operator
    std::strcpy(p->name, "John Doe");
    p->age = 30;

    // Access and print the values
    std::cout << "Name: " << p->name << std::endl;
    std::cout << "Age: " << p->age << std::endl;

    // Free allocated memory
    delete p;

    return 0;
}
