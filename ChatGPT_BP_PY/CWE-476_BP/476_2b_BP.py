import ctypes
import ctypes.util

# Define the Person struct with ctypes
class Person(ctypes.Structure):
    _fields_ = [("status", ctypes.c_int),
                ("name", ctypes.c_char * 50)]  # Assuming a maximum of 50 characters for the name

def create_person(name: str) -> ctypes.POINTER(Person):
    # Validate the input name to ensure it meets requirements (e.g., not too long)
    if not isinstance(name, str):
        raise ValueError("Name must be a string.")
    
    if len(name) >= 50:
        raise ValueError("Name is too long. Maximum allowed length is 49 characters.")
    
    # Allocate memory for a new Person object
    person_pointer = ctypes.POINTER(Person)(Person())
    
    # Set default values
    person_pointer.contents.status = 0
    
    # Securely copy the name into the allocated memory
    ctypes.memset(person_pointer.contents.name, 0, 50)  # Zero the name field
    ctypes.memmove(person_pointer.contents.name, name.encode('utf-8'), len(name))
    
    return person_pointer

# Test the function
new_person = create_person("John")

# Accessing struct members via the pointer
print(f"Person status: {new_person.contents.status}")
print(f"Person name: {new_person.contents.name.decode('utf-8')}")

# Clean up: In Python, we rely on garbage collection, but if this were C, you'd need to free the memory manually.