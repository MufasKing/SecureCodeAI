import hashlib



def calculate_checksum(data):

    """Calculate MD5 checksum of the given data."""

    md5_hash = hashlib.md5()

    md5_hash.update(data)

    return md5_hash.hexdigest()



def read_file_contents(file_path):

    """Read the contents of a file."""

    try:

        with open(file_path, 'rb') as file:

            return file.read()

    except FileNotFoundError:

        print(f"The file {file_path} does not exist.")

        return None

    except IOError as e:

        print(f"An error occurred while reading the file {file_path}: {e}")

        return None



def write_results_to_file(file_path, bytes_read, checksum):

    """Write the number of bytes read and the checksum to another file."""

    try:

        with open(file_path, 'w') as file:

            file.write(f"Bytes Read: {bytes_read}Checksum: {checksum}")

    except IOError as e:

        print(f"An error occurred while writing to the file {file_path}: {e}")



def process_file(input_file_path, output_file_path):

    """Process the input file, calculate its checksum, and write the results."""

    # Input validation

    if not isinstance(input_file_path, str) or not isinstance(output_file_path, str):

        print("Invalid input: file paths must be strings.")

        return



    # Read the contents of the file

    buffer = read_file_contents(input_file_path)

    if buffer is None:

        return  # Error reading file, exit early



    # Calculate checksum

    checksum = calculate_checksum(buffer)

    bytes_read = len(buffer)



    # Check if buffer is empty

    if bytes_read == 0:

        print("The buffer is empty.")

        checksum = '0'  # Setting checksum to '0' to indicate empty buffer



    # Write the results to another file

    write_results_to_file(output_file_path, bytes_read, checksum)



# Example usage

input_file_path = 'path/to/input/file'

output_file_path = 'path/to/output/file'

process_file(input_file_path, output_file_path)