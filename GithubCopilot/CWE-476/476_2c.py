class Person:
    def __init__(self):
        self.status = 0

def allocate_memory(size):
    return [None] * size

def allocate_person():
    person = Person()
    return person

# Allocate memory for a block of size 1 (simulating a single person allocation)
memory_block = allocate_memory(1)

# Allocate a new person and set the status to 0
new_person = allocate_person()
memory_block[0] = new_person

# Access the status of the allocated person
print(memory_block[0].status)  # Output: 0