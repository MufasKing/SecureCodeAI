import ctypes

# Define the Person struct
class Person(ctypes.Structure):
    _fields_ = [("name", ctypes.c_char_p),
                ("age", ctypes.c_int)]

# Function to allocate memory for a Person instance
def allocate_person(name: str, age: int) -> ctypes.POINTER(Person):
    # Allocate memory for a Person instance
    person_ptr = ctypes.pointer(Person())
    
    # Set the fields
    person_ptr.contents.name = name.encode('utf-8')
    person_ptr.contents.age = age
    
    return person_ptr

# Example usage
person = allocate_person("John Doe", 30)

# Accessing members using the pointer
print(f"Name: {person.contents.name.decode('utf-8')}")
print(f"Age: {person.contents.age}")