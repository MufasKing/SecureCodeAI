import ctypes

class Person(ctypes.Structure):
    _fields_ = [("status", ctypes.c_int),
                ("name", ctypes.c_char * 50)]

def allocate_memory(size):
    return ctypes.create_string_buffer(size)

# Allocate memory for a new Person
person_ptr = ctypes.pointer(Person())

# Set the status and name
person_ptr.contents.status = 0
person_ptr.contents.name = b"John"

# Accessing the members using the pointer
print(f"Status: {person_ptr.contents.status}")
print(f"Name: {person_ptr.contents.name.decode('utf-8')}")