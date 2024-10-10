import ctypes

# Define a Person structure using ctypes
class Person(ctypes.Structure):
    _fields_ = [("status", ctypes.c_int),
                ("name", ctypes.c_char_p)]

def create_person(name="John"):
    # Allocate memory for a new Person
    person = Person()
    person_pointer = ctypes.pointer(person)
    
    # Perform input validation
    if not isinstance(name, str):
        raise ValueError("Name must be a string")
    
    # Secure data handling
    try:
        # Set the person's name and status
        person_pointer.contents.name = name.encode('utf-8')  # Convert string to bytes
        person_pointer.contents.status = 0
    except Exception as e:
        print(f"Error setting person's attributes: {e}")
        # Optionally, deallocate memory here if needed
        return None
    
    return person_pointer

# Example usage
person_ptr = create_person("John")
if person_ptr:
    print(f"Created person with name: {person_ptr.contents.name.decode('utf-8')}, status: {person_ptr.contents.status}")