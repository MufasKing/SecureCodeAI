import subprocess
import shlex

def execute_ls_command(directory: str) -> None:
    # Input validation and sanitization
    if not isinstance(directory, str):
        raise ValueError("The directory must be a string.")
    
    # Remove any unsafe characters
    sanitized_directory = shlex.quote(directory)
    
    # Construct the command securely
    command = f'ls {sanitized_directory}'
    
    try:
        # Execute the command securely using subprocess
        result = subprocess.run(shlex.split(command), check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
    except FileNotFoundError:
        print("Command not found. Ensure 'ls' is available.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
execute_ls_command("/path/to/directory")