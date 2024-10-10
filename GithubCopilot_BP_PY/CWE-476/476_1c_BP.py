import ctypes

# Define a class for our person structure
class Person(ctypes.Structure):
    _fields_ = [("name", ctypes.c_char_p),
                ("age", ctypes.c_int),
                ("status", ctypes.c_int)]

def allocate_person():
    # Allocate memory for a person
    person_ptr = ctypes.pointer(Person())
    
    # Initialize the person's status to 0
    person_ptr.contents.status = 0
    
    return person_ptr

def deallocate_person(person_ptr):
    # Deallocate the memory for the person
    # In Python, ctypes automatically manages memory for ctypes objects,
    # so explicit deallocation is not typically necessary.
    # However, for educational purposes or specific use cases, you might use:
    del person_ptr

def set_person_name(person_ptr, name):
    # Set the person's name, ensuring the name is a bytes object for ctypes compatibility
    if isinstance(name, str):
        name = name.encode('utf-8')
    person_ptr.contents.name = name

def main():
    try:
        person_ptr = allocate_person()
        set_person_name(person_ptr, "John Doe")
        print(f"Allocated a person with status: {person_ptr.contents.status}")
        
        # Always ensure to deallocate or manage memory properly to avoid leaks
        # In this case, deallocation is handled by Python's garbage collector.
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # If explicit deallocation was necessary or implemented, it would go here.
        pass

if __name__ == "__main__":
    main()