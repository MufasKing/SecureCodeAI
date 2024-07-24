import ctypes

# Define a struct representing a person
class Person(ctypes.Structure):
    _fields_ = [
        ('name', ctypes.c_char_p),
        ('age', ctypes.c_int),
        ('status', ctypes.c_int)
    ]

# Function to allocate memory and create a new person
def create_person(name, age):
    # Allocate memory for a Person struct
    p = ctypes.POINTER(Person)
    person_ptr = ctypes.cast(ctypes.c_char_p(ctypes.create_string_buffer(ctypes.sizeof(Person))), p)

    # Access the struct fields and set initial values
    person_ptr.contents.name = ctypes.c_char_p(name.encode())
    person_ptr.contents.age = age
    person_ptr.contents.status = 0

    return person_ptr

# Function to deallocate memory of a person
def delete_person(person_ptr):
    ctypes.cast(person_ptr, ctypes.POINTER(ctypes.c_char)).free()

# Example usage
if __name__ == '__main__':
    # Create a new person
    person = create_person("John Doe", 30)

    # Access and print person details
    print(f"Name: {person.contents.name.decode()}, Age: {person.contents.age}, Status: {person.contents.status}")

    # Deallocate memory
    delete_person(person)