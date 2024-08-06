import hashlib

import os



def read_file_and_calculate_checksum(file_path):

    # Input validation for file path

    if not os.path.isfile(file_path):

        raise ValueError("File does not exist")



    try:

        # Reading the contents of the file into a buffer

        with open(file_path, 'rb') as file:

            buffer = file.read()

        

        # Calculating the checksum of the buffer using SHA-256 for secure hashing

        checksum = hashlib.sha256(buffer).hexdigest()

        

        # If the checksum is 0, the buffer is empty (though practically, SHA-256 checksum will never be 0)

        if int(checksum, 16) == 0:

            raise ValueError("Buffer is empty")

        

        # Saving the number of bytes read and the checksum to a file

        with open("checksum_info.txt", 'w') as output_file:

            output_file.write(f"Bytes read: {len(buffer)}Checksum: {checksum}")

            

    except IOError as e:

        # Exception handling for file management errors

        print(f"An error occurred while reading or writing files: {e}")

    except Exception as e:

        # General exception handling

        print(f"An unexpected error occurred: {e}")



# Example usage

file_path = "example.txt"

read_file_and_calculate_checksum(file_path)