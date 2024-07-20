import ctypes

# Define a C-style structure using ctypes
class Person(ctypes.Structure):
    _fields_ = [("name", ctypes.c_char * 50),  # Fixed-size array for name
                ("age", ctypes.c_int)]

# Allocate memory for an instance of Person
def allocate_person():
    # Create an instance of Person
    person = Person()
    # Allocate memory for the Person structure
    person_pointer = ctypes.pointer(person)
    return person_pointer

def main():
    # Allocate memory and get a pointer to a Person structure
    person_ptr = allocate_person()
    
    # Access the members of the Person structure
    person = person_ptr.contents
    
    # Set values
    person.name = b"John Doe"  # Use bytes for C strings
    person.age = 30
    
    # Print values
    print(f"Name: {person.name.decode('utf-8')}")  # Decode bytes to string
    print(f"Age: {person.age}")

if __name__ == "__main__":
    main()
