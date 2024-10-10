import os

def read_file_from_safe_directory(filename):
    # Define the safe directory path
    safe_directory = 'safe_directory'
    
    # Construct the full file path
    file_path = os.path.join(safe_directory, filename)
    
    # Check if the file exists and is a file
    if os.path.isfile(file_path):
        try:
            # Open and read the file
            with open(file_path, 'r') as file:
                content = file.read()
                return content
        except IOError as e:
            print(f"Error reading the file: {e}")
    else:
        print(f"The file does not exist or is not a file: {file_path}")

# Example usage
filename = 'example.txt'  # Replace with your actual filename
file_content = read_file_from_safe_directory(filename)
if file_content is not None:
    print(file_content)
