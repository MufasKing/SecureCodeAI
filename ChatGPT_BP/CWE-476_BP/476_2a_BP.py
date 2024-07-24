import ctypes

# Define a C-like struct for Person
class Person(ctypes.Structure):
    _fields_ = [("status", ctypes.c_int)]

# Allocate memory for a Person instance and return a pointer to it
def allocate_person():
    # Allocate memory for a single Person structure
    person_ptr = ctypes.pointer(Person())

    # Initialize the 'status' field to 0
    person_ptr.contents.status = 0
    
    return person_ptr

# Free allocated memory (not strictly necessary in Python due to garbage collection)
def free_person(person_ptr):
    # Set the pointer to None, allowing Python's garbage collector to reclaim the memory
    person_ptr = None

# Example usage
if __name__ == "__main__":
    # Allocate a new person
    new_person = allocate_person()
    
    # Access and print the 'status' field
    print(f"Person status: {new_person.contents.status}")
    
    # Clean up memory
    free_person(new_person)