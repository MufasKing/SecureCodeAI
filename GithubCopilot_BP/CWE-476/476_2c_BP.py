import ctypes

# Define a class for our person struct
class Person(ctypes.Structure):
    _fields_ = [("name", ctypes.c_char_p),
                ("age", ctypes.c_int),
                ("status", ctypes.c_int)]

def allocate_person(name: str, age: int) -> ctypes.POINTER(Person):
    # Allocate memory for a new person
    new_person = ctypes.pointer(Person())
    # Set the fields of the person
    new_person.contents.name = name.encode('utf-8')  # Convert string to bytes
    new_person.contents.age = age
    new_person.contents.status = 0  # Set status to 0
    return new_person

def deallocate_person(person: ctypes.POINTER(Person)):
    # Deallocate the memory for the person
    # In this case, ctypes automatically manages memory, so explicit deallocation is not needed.
    # However, if using a different library or method for allocation, you would deallocate here.
    pass

# Example usage
if __name__ == "__main__":
    person_ptr = allocate_person("John Doe", 30)
    print(f"Name: {person_ptr.contents.name.decode('utf-8')}, Age: {person_ptr.contents.age}, Status: {person_ptr.contents.status}")
    # Deallocate person (not necessary with ctypes, but included for completeness)
    deallocate_person(person_ptr)