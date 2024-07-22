import os

def read_file(filename):
    # Define the path to the /safe/ directory
    safe_directory = '/safe/'
    
    # Create the full file path
    file_path = os.path.join(safe_directory, filename)
    
    # Check if the file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file '{filename}' does not exist in the directory '{safe_directory}'.")
    
    # Read the file content
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except IOError as e:
        raise RuntimeError(f"An error occurred while reading the file: {e}")

# Example usage
if __name__ == "__main__":
    filename = 'example.txt'  # Replace with the actual file name you want to read
    try:
        file_content = read_file(filename)
        print(file_content)
    except Exception as e:
        print(e)
