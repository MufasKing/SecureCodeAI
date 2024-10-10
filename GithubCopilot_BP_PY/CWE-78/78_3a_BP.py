import subprocess
import shlex

def secure_ls_command(directory):
    """
    Executes the 'ls' command securely on the specified directory, ensuring input sanitization,
    secure subprocess execution, error handling, and adherence to the principle of least privilege.
    
    Parameters:
    directory (str): The directory to list contents of.
    """
    # Input sanitization
    if not isinstance(directory, str):
        raise ValueError("Directory path must be a string.")
    sanitized_directory = shlex.quote(directory)
    
    # Secure subprocess execution with error handling
    try:
        # Using subprocess.run for secure execution, avoiding shell=True
        result = subprocess.run(["ls", sanitized_directory], text=True, capture_output=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while trying to list the contents of {sanitized_directory}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
secure_ls_command("/path/to/directory")