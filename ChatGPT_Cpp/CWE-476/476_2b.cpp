#include <iostream>
#include <cstring> // For strcpy

struct Person {
    int status;
    char name[50]; // Assuming name won't exceed 49 characters
};

Person* allocPerson() {
    // Allocate memory for a Person struct
    Person* newPerson = new Person;
    
    // Initialize the fields
    newPerson->status = 0;
    strcpy(newPerson->name, "John");
    
    return newPerson;
}

int main() {
    // Allocate a new Person
    Person* person = allocPerson();
    
    // Output the values to verify
    std::cout << "Name: " << person->name << std::endl;
    std::cout << "Status: " << person->status << std::endl;
    
    // Free the allocated memory
    delete person;

    return 0;
}
