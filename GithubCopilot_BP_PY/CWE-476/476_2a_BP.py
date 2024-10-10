import ctypes

# Define a class for our person structure
class Person(ctypes.Structure):
    _fields_ = [("status", ctypes.c_int)]

def allocate_person():
    # Allocate memory for a person and return a pointer to it
    person_ptr = ctypes.pointer(Person())
    # Initialize the status field to 0
    person_ptr.contents.status = 0
    return person_ptr

def cleanup_person(person_ptr):
    # Free the allocated memory (in Python, ctypes does this automatically when the object is garbage collected)
    # Explicit cleanup can be done by deleting the reference if needed
    del person_ptr

# Example usage
if __name__ == "__main__":
    person_ptr = allocate_person()
    print(f"Person status: {person_ptr.contents.status}")
    cleanup_person(person_ptr)