import hashlib

import os



def read_file(file_path):

    """

    Reads the content of a file and returns it as bytes.



    :param file_path: Path to the file to be read

    :return: File content as bytes

    """

    try:

        if not os.path.isfile(file_path):

            raise FileNotFoundError(f"File '{file_path}' not found.")



        with open(file_path, 'rb') as file:

            data = file.read()

            return data

    except Exception as e:

        raise IOError(f"Error reading file '{file_path}': {e}")



def calculate_checksum(data):

    """

    Calculates the SHA-256 checksum of the given data.



    :param data: Data in bytes

    :return: SHA-256 checksum as a hexadecimal string

    """

    try:

        if not isinstance(data, bytes):

            raise ValueError("Data must be in bytes.")



        sha256_hash = hashlib.sha256()

        sha256_hash.update(data)

        return sha256_hash.hexdigest()

    except Exception as e:

        raise ValueError(f"Error calculating checksum: {e}")



def write_results(output_path, num_bytes, checksum):

    """

    Writes the number of bytes and checksum to an output file.



    :param output_path: Path to the output file

    :param num_bytes: Number of bytes read from the input file

    :param checksum: Checksum of the input file

    """

    try:

        with open(output_path, 'w') as file:

            file.write(f"Bytes read: {num_bytes}")

            file.write(f"Checksum: {checksum}")

    except Exception as e:

        raise IOError(f"Error writing to file '{output_path}': {e}")



def main(input_file, output_file):

    """

    Main function to read file, calculate checksum, and save the results.



    :param input_file: Path to the input file to read

    :param output_file: Path to the output file to save results

    """

    try:

        # Validate file paths

        if not input_file or not isinstance(input_file, str):

            raise ValueError("Input file path is not valid.")

        if not output_file or not isinstance(output_file, str):

            raise ValueError("Output file path is not valid.")



        # Read file content

        data = read_file(input_file)

        num_bytes = len(data)



        # Calculate checksum

        checksum = calculate_checksum(data)



        # If checksum is equivalent to an empty file, override it to indicate empty buffer

        if checksum == hashlib.sha256(b'').hexdigest():

            print("The buffer is empty (checksum is 0).")



        # Write results to the output file

        write_results(output_file, num_bytes, checksum)



        print(f"Results saved to '{output_file}'")



    except Exception as e:

        print(f"An error occurred: {e}")



if __name__ == "__main__":

    input_file = 'path/to/input/file.txt'

    output_file = 'path/to/output/file.txt'

    main(input_file, output_file)