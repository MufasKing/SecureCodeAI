import ctypes

# Define a struct representation for 'person'
class Person(ctypes.Structure):
    _fields_ = [("name", ctypes.c_char_p),
                ("age", ctypes.c_int)]

# Memory allocation method
def allocate_person():
    # Allocate a block of memory of size sizeof(Person)
    person_ptr = ctypes.cast(ctypes.create_string_buffer(ctypes.sizeof(Person)), ctypes.POINTER(Person))
    return person_ptr

# Proper initialization of a person instance
def initialize_person(person_ptr, name, age):
    # Using the -> operator equivalent in Python to access and set members of the struct through a pointer
    person_ptr.contents.name = name.encode('utf-8')  # Encoding string to bytes
    person_ptr.contents.age = age

# Memory deallocation method
def deallocate_person(person_ptr):
    # In Python, ctypes automatically manages memory deallocation for objects created via ctypes
    # However, if you were manually managing memory (e.g., using malloc from libc), you would use ctypes to call free
    pass  # Placeholder to indicate where deallocation code would go if needed

# Example usage
if __name__ == "__main__":
    person_ptr = allocate_person()
    initialize_person(person_ptr, "John Doe", 30)
    print(f"Name: {person_ptr.contents.name.decode('utf-8')}, Age: {person_ptr.contents.age}")
    deallocate_person(person_ptr)