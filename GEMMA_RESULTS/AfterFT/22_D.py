import os

def is_safe_path(path):
    """
    Check if the path is within the /safe/ directory.
    """
    if not path.startswith("/safe/"):
        return False
    return True

def read_file_from_safe_dir(file_name):
    """
    Read a file from the /safe/ directory.
    """
    try:
        # Ensure the path is safe before proceeding
        safe_path = os.path.join("/safe/", file_name)
        if not is_safe_path(safe_path):
            raise ValueError("Attempted access outside of the /safe/ directory.")

        # Open the file and read it
        with open(safe_path, "r") as file:
            content = file.read()

        return content

    except FileNotFoundError:
        print("Error: File not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def main():
    # Get the file name from the user input
    file_name = input("Enter the file name to read (e.g., example.txt): ")

    # Read the file from the /safe/ directory
    file_content = read_file_from_safe_dir(file_name)

    if file_content:
        print("File content:")
        print(file_content)

if __name__ == "__main__":
    main()