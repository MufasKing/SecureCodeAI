import ctypes

# Define the structure
class Person(ctypes.Structure):
    _fields_ = [("id", ctypes.c_int),
                ("status", ctypes.c_int)]

# Allocate memory for a new person instance
new_person = Person()

# Set the status to 0
new_person.status = 0

# Access the status
print("Status:", new_person.status)

# To mimic the use of pointers and the '->' operator in C
# We just use the attribute access in Python

# Create a pointer to the person instance
person_ptr = ctypes.pointer(new_person)

# Access fields using the pointer (mimicking `person_ptr->status` in C)
print("Status via pointer:", person_ptr.contents.status)
