class Person:
    def __init__(self):
        self.status = 0

def allocate_person():
    return Person()

# Allocate a new person and set the status to 0
new_person = allocate_person()
print(new_person.status)  # Output should be 0