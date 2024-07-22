<<<<<<< HEAD
def memcpy(dest, src, num_bytes):

    """

    Copy num_bytes from src to dest.

    

    Parameters:

    dest (bytearray): The destination buffer.

    src (bytearray): The source buffer.

    num_bytes (int): Number of bytes to copy.

    """

    # Input Validation

    if not isinstance(dest, bytearray):

        raise ValueError("Destination must be a bytearray")

    if not isinstance(src, (bytes, bytearray)):

        raise ValueError("Source must be bytes or bytearray")

    if not isinstance(num_bytes, int) or num_bytes < 0:

        raise ValueError("Number of bytes must be a non-negative integer")

    if num_bytes > len(src):

        raise ValueError("Number of bytes to copy exceeds source length")

    if num_bytes > len(dest):

        raise ValueError("Number of bytes to copy exceeds destination length")



    # Clear Destination Buffer

    dest[:num_bytes] = b'' * num_bytes



    # Copy bytes from src to dest

    for i in range(num_bytes):

        dest[i] = src[i]



def strlen(s):

    """

    Calculate the length of a string in a secure manner.

    

    Parameters:

    s (str): The input string.

    

    Returns:

    int: The length of the string.

    """

    # Input Validation

    if not isinstance(s, str):

        raise ValueError("Input must be a string")

    

    # Secure Length Calculation

    length = 0

    for char in s:

        length += 1

    

    return length



# Example usage

src_string = "Hello"

src_bytes = bytearray(src_string, 'utf-8')

dest_buffer = bytearray(len(src_bytes))



# Securely calculate length of the source string

length_of_src = strlen(src_string)



# Copy the string to the buffer

memcpy(dest_buffer, src_bytes, length_of_src)



# Verify the copy

print("Source String:", src_string)

=======
def memcpy(dest, src, num_bytes):

    """

    Copy num_bytes from src to dest.

    

    Parameters:

    dest (bytearray): The destination buffer.

    src (bytearray): The source buffer.

    num_bytes (int): Number of bytes to copy.

    """

    # Input Validation

    if not isinstance(dest, bytearray):

        raise ValueError("Destination must be a bytearray")

    if not isinstance(src, (bytes, bytearray)):

        raise ValueError("Source must be bytes or bytearray")

    if not isinstance(num_bytes, int) or num_bytes < 0:

        raise ValueError("Number of bytes must be a non-negative integer")

    if num_bytes > len(src):

        raise ValueError("Number of bytes to copy exceeds source length")

    if num_bytes > len(dest):

        raise ValueError("Number of bytes to copy exceeds destination length")



    # Clear Destination Buffer

    dest[:num_bytes] = b'' * num_bytes



    # Copy bytes from src to dest

    for i in range(num_bytes):

        dest[i] = src[i]



def strlen(s):

    """

    Calculate the length of a string in a secure manner.

    

    Parameters:

    s (str): The input string.

    

    Returns:

    int: The length of the string.

    """

    # Input Validation

    if not isinstance(s, str):

        raise ValueError("Input must be a string")

    

    # Secure Length Calculation

    length = 0

    for char in s:

        length += 1

    

    return length



# Example usage

src_string = "Hello"

src_bytes = bytearray(src_string, 'utf-8')

dest_buffer = bytearray(len(src_bytes))



# Securely calculate length of the source string

length_of_src = strlen(src_string)



# Copy the string to the buffer

memcpy(dest_buffer, src_bytes, length_of_src)



# Verify the copy

print("Source String:", src_string)

>>>>>>> ba676d116bd92de16bbd8430dcbd7b419c5f8d74
print("Destination Buffer:", dest_buffer.decode('utf-8'))