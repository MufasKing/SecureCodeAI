import ctypes

# Define the Person struct
class Person(ctypes.Structure):
    _fields_ = [("name", ctypes.c_char * 50),  # Example field
                ("age", ctypes.c_int),         # Example field
                ("status", ctypes.c_int)]      # Field to be set to 0

# Function to allocate memory for a Person and set status to 0
def allocate_person():
    # Allocate memory for one Person
    person = Person()
    
    # Set the status field to 0
    person.status = 0
    
    return person

# Example usage
if __name__ == "__main__":
    # Allocate and initialize the Person
    new_person = allocate_person()
    
    # Print out the status to verify it's set correctly
    print(f"Person status: {new_person.status}")
