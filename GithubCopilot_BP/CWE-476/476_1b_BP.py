# Include necessary libraries
import ctypes

# Define the person structure
class Person(ctypes.Structure):
    _fields_ = [("name", ctypes.c_char_p),
                ("age", ctypes.c_int),
                ("status", ctypes.c_int)]

def allocate_person():
    # Allocate memory for a new person
    person_ptr = ctypes.cast(ctypes.create_string_buffer(ctypes.sizeof(Person)), ctypes.POINTER(Person))
    
    # Initialize the person's status to 0
    person_ptr.contents.status = 0
    
    return person_ptr

def deallocate_person(person_ptr):
    # Deallocate the memory block pointed by person_ptr
    # In Python, ctypes automatically manages memory for ctypes objects, so explicit deallocation is not necessary.
    # However, for educational purposes, we'll set the pointer to None to simulate deallocation.
    person_ptr = None

def set_person_data(person_ptr, name, age):
    # Set the person's data
    if person_ptr:
        person_ptr.contents.name = name.encode('utf-8')
        person_ptr.contents.age = age
    else:
        print("Error: Invalid person pointer")

def get_person_data(person_ptr):
    # Get the person's data
    if person_ptr:
        return {
            "name": person_ptr.contents.name.decode('utf-8'),
            "age": person_ptr.contents.age,
            "status": person_ptr.contents.status
        }
    else:
        print("Error: Invalid person pointer")
        return None

# Example usage
if __name__ == "__main__":
    person_ptr = allocate_person()
    set_person_data(person_ptr, "John Doe", 30)
    person_data = get_person_data(person_ptr)
    print(person_data)
    deallocate_person(person_ptr)