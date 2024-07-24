import ctypes

# Define the Person structure
class Person(ctypes.Structure):
    _fields_ = [
        ("status", ctypes.c_int),
        ("name", ctypes.c_char * 50)  # Assuming name is a string with a max length of 50 characters
    ]

# Allocate memory and create a new Person
new_person = Person()

# Set the 'status' to 0
new_person.status = 0

# Set the 'name' to "John"
# The ctypes.c_char array requires a byte string. Encode "John" to bytes and ensure it's null-terminated.
new_person.name = b"John"

# Print the details to verify
print(f"Status: {new_person.status}")
print(f"Name: {new_person.name.decode('utf-8')}")
