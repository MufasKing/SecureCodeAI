import ctypes

# Define a C-like structure in Python using ctypes
class Person(ctypes.Structure):
    _fields_ = [("status", ctypes.c_int)]

def allocate_person():
    try:
        # Allocate memory for a Person structure
        person_ptr = ctypes.pointer(Person())

        # Set the status to 0
        person_ptr.contents.status = 0

        print(f"Person status: {person_ptr.contents.status}")

        # Return the pointer to the allocated person
        return person_ptr
    except MemoryError:
        print("Memory allocation failed!")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def free_person(person_ptr):
    try:
        # Deallocate memory by simply removing reference
        del person_ptr
        print("Memory deallocated successfully.")
    except Exception as e:
        print(f"An error occurred during deallocation: {e}")

if __name__ == "__main__":
    # Allocate a new Person
    person = allocate_person()
    
    if person is not None:
        # Use the person for something
        print(f"Person created with status: {person.contents.status}")
        
        # Deallocate the Person
        free_person(person)
    else:
        print("Failed to allocate Person.")