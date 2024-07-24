import ctypes

# Define the C-like struct using ctypes
class Person(ctypes.Structure):
    _fields_ = [("status", ctypes.c_int)]

# Function to allocate a new Person and set the status to 0
def allocate_person():
    # Allocate a new Person instance
    person = Person()
    
    # Set the status to 0
    person.status = 0
    
    # Return a pointer to the allocated memory
    return ctypes.pointer(person)

# Allocate memory for a new Person and get the pointer
person_pointer = allocate_person()

# Access the members of the Person struct using the pointer
print(f"Person status: {person_pointer.contents.status}")

# Modify the status using the pointer
person_pointer.contents.status = 1
print(f"Updated Person status: {person_pointer.contents.status}")
