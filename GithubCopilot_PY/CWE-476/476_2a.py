import ctypes

# Define the person struct
class Person(ctypes.Structure):
    _fields_ = [("status", ctypes.c_int)]

# Allocate memory for a new person
new_person = ctypes.pointer(Person())

# Set the status to 0
new_person.contents.status = 0

# Print the status to verify
print(new_person.contents.status)