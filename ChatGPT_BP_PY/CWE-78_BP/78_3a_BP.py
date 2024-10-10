import subprocess
import shlex
import os

def execute_ls(directory):
    # Input sanitization
    directory = shlex.quote(directory)
    
    # Define the command
    command = f"ls {directory}"
    
    try:
        # Secure subprocess execution
        result = subprocess.run(shlex.split(command), check=True, capture_output=True, text=True)
        
        # Print the output
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
if __name__ == "__main__":
    # Assuming we are using least privilege principle, for example, we will run this as a non-root user.
    # Example directory input - normally you would get this from user input in a real application
    directory_input = "/path/to/directory"
    execute_ls(directory_input)