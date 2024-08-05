import hashlib

def calculate_checksum(buffer):
    return hashlib.md5(buffer).hexdigest()

def process_file(input_file_path, output_file_path):
    # Read the contents of the input file into a buffer
    with open(input_file_path, 'rb') as input_file:
        buffer = input_file.read()
    
    # Calculate the checksum of the buffer
    checksum = calculate_checksum(buffer)
    
    # Check if the buffer is empty
    if checksum == hashlib.md5(b'').hexdigest():
        print("The buffer is empty.")
    
    # Get the number of bytes read
    num_bytes_read = len(buffer)
    
    # Write the number of bytes read and the checksum to the output file
    with open(output_file_path, 'w') as output_file:
        output_file.write(f"Number of bytes read: {num_bytes_read}\n")
        output_file.write(f"Checksum: {checksum}\n")

# Example usage
input_file_path = 'input.txt'
output_file_path = 'output.txt'
process_file(input_file_path, output_file_path)