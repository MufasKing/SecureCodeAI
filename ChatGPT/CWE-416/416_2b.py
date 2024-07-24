import hashlib

def calculate_checksum(data):
    """Calculate the checksum of the given data."""
    # Use SHA-256 for a checksum
    checksum = hashlib.sha256(data).hexdigest()
    return checksum

def main(input_file, output_file):
    """Read the input file, calculate checksum, and write results to the output file."""
    try:
        # Read the contents of the input file into a buffer
        with open(input_file, 'rb') as file:
            buffer = file.read()
        
        # Calculate checksum of the buffer
        checksum = calculate_checksum(buffer)
        
        # Determine if the buffer is empty based on checksum
        is_empty = (checksum == 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855') # SHA-256 for an empty buffer
        
        # Number of bytes read
        num_bytes = len(buffer)
        
        # Write the number of bytes and checksum to the output file
        with open(output_file, 'w') as file:
            file.write(f'Number of bytes read: {num_bytes}\n')
            file.write(f'Checksum: {checksum}\n')
            file.write(f'Buffer is empty: {"Yes" if is_empty else "No"}\n')
        
        print(f'Processed file "{input_file}" and wrote results to "{output_file}".')
    
    except FileNotFoundError:
        print(f'Error: The file "{input_file}" was not found.')
    except IOError as e:
        print(f'Error: An I/O error occurred. Details: {e}')

# Example usage
input_file = 'input.txt'  # Replace with the path to your input file
output_file = 'output.txt'  # Replace with the path to your output file

main(input_file, output_file)
