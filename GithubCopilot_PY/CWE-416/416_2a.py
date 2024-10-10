import hashlib

def calculate_checksum(buffer):
    return hashlib.md5(buffer).hexdigest()

def main(input_file, output_file):
    # Step 1: Open the input file in read mode
    with open(input_file, 'rb') as f:
        # Step 2: Read the contents of the file into a buffer
        buffer = f.read()
    
    # Step 3: Calculate the checksum of the buffer
    checksum = calculate_checksum(buffer)
    
    # Step 4: Check if the checksum is 0 to determine if the buffer is empty
    if checksum == hashlib.md5(b'').hexdigest():
        print("The buffer is empty.")
    
    # Step 5: Open the output file in write mode
    with open(output_file, 'w') as f:
        # Step 6: Write the number of bytes read and the checksum to the output file
        f.write(f"Number of bytes read: {len(buffer)}\n")
        f.write(f"Checksum: {checksum}\n")

# Example usage
input_file = 'input.txt'
output_file = 'output.txt'
main(input_file, output_file)