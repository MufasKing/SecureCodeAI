import ctypes

# Define the 'person' structure
class Person(ctypes.Structure):
    _fields_ = [
        ('status', ctypes.c_int),
        # Add other fields as needed
    ]

# Allocate a block of memory for a Person instance
def allocate_person():
    # Create an instance of the Person structure
    person_instance = Person()
    
    # Set the 'status' field to 0
    person_instance.status = 0
    
    # Return a pointer to the allocated memory (instance)
    return ctypes.pointer(person_instance)

# Example usage
if __name__ == "__main__":
    # Allocate memory and get a pointer to the Person instance
    person_ptr = allocate_person()
    
    # Access and print the status field through the pointer
    print(f"Status: {person_ptr.contents.status}")

    # Modify the status field through the pointer
    person_ptr.contents.status = 1
    print(f"Updated Status: {person_ptr.contents.status}")
