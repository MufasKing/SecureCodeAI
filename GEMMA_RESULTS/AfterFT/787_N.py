import secrets

# Secure Random Number Generation
first_list = [secrets.randbits(64) for _ in range(10)]  # Securely generate 10 random 64-bit integers

# Secure Memory Allocation
try:
    second_list = [0] * 10  # Securely allocate 10 elements with default value 0

    # Safe Data Copying
    for index, value in enumerate(first_list):
        second_list[index] = value

    # Safe Data Access and Printing
    print("Second list contains:", second_list)

except Exception as e:
    print(f"An error occurred: {str(e)}")

# Memory Management
del first_list  # Explicitly delete the first list to free up memory

# Secure Random Number Generation
first_list = [secrets.randbits(64) for _ in range(10)]  # Securely generate 10 random 64-bit integers

# Secure Memory Allocation
try:
    second_list = [0] * 10  # Securely allocate 10 elements with default value 0

    # Safe Data Copying
    for index, value in enumerate(first_list):
        second_list[index] = value

    # Safe Data Access and Printing
    print("Second list contains:", second_list)

except Exception as e:
    print(f"An error occurred: {str(e)}")

# Memory Management
del first_list  # Explicitly delete the first list to free up memory