import hashlib

def calculate_checksum(data: bytes) -> str:
    """Calculate the checksum of the given data."""
    return hashlib.md5(data).hexdigest()

def process_file(input_file: str, output_file: str):
    try:
        # Read the contents of the input file into a buffer
        with open(input_file, 'rb') as file:
            buffer = file.read()
        
        # Calculate the checksum of the buffer
        checksum = calculate_checksum(buffer)
        
        # Check if the buffer is empty by verifying if checksum is 0
        if checksum == 'd41d8cd98f00b204e9800998ecf8427e':
            print("The buffer is empty.")
        
        # Save the number of bytes read and checksum to the output file
        with open(output_file, 'w') as file:
            file.write(f"Number of bytes read: {len(buffer)}\n")
            file.write(f"Checksum (MD5): {checksum}\n")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except IOError as e:
        print(f"Error: An I/O error occurred. {e}")

# Example usage
input_file = 'input.txt'  # Replace with your input file path
output_file = 'output.txt'  # Replace with your output file path

process_file(input_file, output_file)
