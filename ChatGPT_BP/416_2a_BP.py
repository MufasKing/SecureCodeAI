<<<<<<< HEAD
import hashlib

import os

import sys



def calculate_checksum(buffer):

    """Calculates SHA-256 checksum of the buffer."""

    hasher = hashlib.sha256()

    hasher.update(buffer)

    return hasher.hexdigest()



def read_file_to_buffer(file_path):

    """Reads contents of a file into a buffer."""

    try:

        if not os.path.isfile(file_path):

            raise ValueError(f"File {file_path} does not exist.")

        with open(file_path, 'rb') as file:

            buffer = file.read()

            return buffer

    except IOError as e:

        print(f"Error reading file: {e}")

        raise



def save_checksum_and_size(file_path, num_bytes, checksum):

    """Writes the number of bytes and checksum to a file."""

    try:

        with open(file_path, 'w') as file:

            file.write(f"Bytes read: {num_bytes} Checksum: {checksum}")

    except IOError as e:

        print(f"Error writing to file: {e}")

        raise



def main(input_file_path, output_file_path):

    """Main function to read file, calculate checksum, and save results."""

    try:

        # Validate file paths

        if not input_file_path or not isinstance(input_file_path, str):

            raise ValueError("Invalid input file path.")

        if not output_file_path or not isinstance(output_file_path, str):

            raise ValueError("Invalid output file path.")



        # Read file contents into buffer

        buffer = read_file_to_buffer(input_file_path)

        num_bytes = len(buffer)



        # Calculate checksum

        checksum = calculate_checksum(buffer)

        if checksum == hashlib.sha256(b'').hexdigest():

            checksum = "0"  # Represents an empty buffer



        # Save results to output file

        save_checksum_and_size(output_file_path, num_bytes, checksum)

        

        print(f"Checksum and size saved to {output_file_path}")

        

    except Exception as e:

        print(f"An error occurred: {e}")



if __name__ == "__main__":

    # Example usage: python script.py input.txt output.txt

    if len(sys.argv) != 3:

        print("Usage: python script.py <input_file_path> <output_file_path>")

        sys.exit(1)



    input_file_path = sys.argv[1]

    output_file_path = sys.argv[2]



=======
import hashlib

import os

import sys



def calculate_checksum(buffer):

    """Calculates SHA-256 checksum of the buffer."""

    hasher = hashlib.sha256()

    hasher.update(buffer)

    return hasher.hexdigest()



def read_file_to_buffer(file_path):

    """Reads contents of a file into a buffer."""

    try:

        if not os.path.isfile(file_path):

            raise ValueError(f"File {file_path} does not exist.")

        with open(file_path, 'rb') as file:

            buffer = file.read()

            return buffer

    except IOError as e:

        print(f"Error reading file: {e}")

        raise



def save_checksum_and_size(file_path, num_bytes, checksum):

    """Writes the number of bytes and checksum to a file."""

    try:

        with open(file_path, 'w') as file:

            file.write(f"Bytes read: {num_bytes} Checksum: {checksum}")

    except IOError as e:

        print(f"Error writing to file: {e}")

        raise



def main(input_file_path, output_file_path):

    """Main function to read file, calculate checksum, and save results."""

    try:

        # Validate file paths

        if not input_file_path or not isinstance(input_file_path, str):

            raise ValueError("Invalid input file path.")

        if not output_file_path or not isinstance(output_file_path, str):

            raise ValueError("Invalid output file path.")



        # Read file contents into buffer

        buffer = read_file_to_buffer(input_file_path)

        num_bytes = len(buffer)



        # Calculate checksum

        checksum = calculate_checksum(buffer)

        if checksum == hashlib.sha256(b'').hexdigest():

            checksum = "0"  # Represents an empty buffer



        # Save results to output file

        save_checksum_and_size(output_file_path, num_bytes, checksum)

        

        print(f"Checksum and size saved to {output_file_path}")

        

    except Exception as e:

        print(f"An error occurred: {e}")



if __name__ == "__main__":

    # Example usage: python script.py input.txt output.txt

    if len(sys.argv) != 3:

        print("Usage: python script.py <input_file_path> <output_file_path>")

        sys.exit(1)



    input_file_path = sys.argv[1]

    output_file_path = sys.argv[2]



>>>>>>> ba676d116bd92de16bbd8430dcbd7b419c5f8d74
    main(input_file_path, output_file_path)