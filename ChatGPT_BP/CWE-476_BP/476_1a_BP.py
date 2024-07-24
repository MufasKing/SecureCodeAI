import ctypes

# Define the Person struct
class Person(ctypes.Structure):
    _fields_ = [("name", ctypes.c_char_p),
                ("age", ctypes.c_int)]

# Memory allocation function
def allocate_person():
    # Allocate memory for a Person instance
    person_ptr = ctypes.pointer(Person())
    return person_ptr

# Memory deallocation function
def deallocate_person(person_ptr):
    # Deallocate memory for the Person instance
    # In ctypes, simply deleting the pointer will deallocate the memory
    del person_ptr

# Initialize the Person struct
def initialize_person(person_ptr, name, age):
    person_ptr.contents.name = ctypes.create_string_buffer(name.encode('utf-8'))
    person_ptr.contents.age = age

# Usage example
if __name__ == "__main__":
    # Allocate memory for a Person instance
    person = allocate_person()
    
    # Initialize the Person instance
    initialize_person(person, "John Doe", 30)
    
    # Access the members of the struct
    print(f"Name: {person.contents.name.decode('utf-8')}")
    print(f"Age: {person.contents.age}")
    
    # Deallocate memory
    deallocate_person(person)