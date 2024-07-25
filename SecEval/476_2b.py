import ctypes

class Person(ctypes.Structure):
    _fields_ = [("name", ctypes.c_char_p),
                ("age", ctypes.c_int),
                ("status", ctypes.c_int)]

def memory_allocation(size):
    try:
        # Allocate memory using the specified size
        person_ptr = ctypes.create_string_buffer(size)
        # Set the name and status fields
        person_ptr.name = "John"
        person_ptr.status = 0
        return person_ptr
    except Exception as e:
        # Log the error and return a null pointer
        print("Error allocating memory: {}".format(e))
        return ctypes.create_string_buffer(0)

# Example usage:
person_ptr = memory_allocation(1024)
if person_ptr:
    print(person_ptr.name)  # prints "John"
    print(person_ptr.status)  # prints 0
else:
    print("Error allocating memory")