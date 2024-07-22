import os



def validate_filename(filename):

    """Validates the filename to ensure it does not contain any restricted characters or path traversal sequences."""

    if not filename:

        raise ValueError("Filename cannot be empty.")

    if any(char in filename for char in ['..', '/', '\\']):

        raise ValueError("Invalid filename: Path traversal detected.")

    return filename



def read_file_from_safe_directory(filename):

    """Reads the content of a file from the /safe/ directory after validating the filename."""

    # Define the safe directory

    safe_directory = '/safe/'



    # Validate the filename

    validated_filename = validate_filename(filename)



    # Construct the full path

    file_path = os.path.join(safe_directory, validated_filename)



    # Read the file content with proper error handling and resource cleanup

    try:

        with open(file_path, 'r') as file:

            content = file.read()

            return content

    except FileNotFoundError:

        print(f"Error: The file '{validated_filename}' does not exist in the /safe/ directory.")

    except IOError as e:

        print(f"Error: An I/O error occurred while reading the file: {e}")



def main():

    # Example usage

    filename = input("Enter the filename to read from /safe/ directory: ")

    try:

        content = read_file_from_safe_directory(filename)

        if content:

            print("File Content:", content)

    except ValueError as ve:

        print(f"Input Validation Error: {ve}")



if __name__ == "__main__":

    main()