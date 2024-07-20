import ctypes

# Define the person struct
class Person(ctypes.Structure):
    _fields_ = [
        ("status", ctypes.c_int)
    ]

# Memory Allocation: Allocate a block of memory for the person struct
try:
    person_pointer = ctypes.POINTER(Person)
    allocated_person = ctypes.cast(ctypes.create_string_buffer(ctypes.sizeof(Person)), person_pointer)

    if not allocated_person:
        raise MemoryError("Memory allocation failed")

    # Set the status field to 0
    allocated_person.contents.status = 0

    # Access and print the status field to confirm
    print(f"Status field set to: {allocated_person.contents.status}")

except MemoryError as e:
    print(f"Error: {e}")

finally:
    # Memory Deallocation
    # In ctypes, memory allocated with create_string_buffer is managed by Python's garbage collector,
    # but we use del to explicitly delete references for clarity.
    del allocated_person