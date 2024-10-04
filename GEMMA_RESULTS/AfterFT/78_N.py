import subprocess
import shlex

def execute_ls(directory):
    # Input validation and sanitization
    if not isinstance(directory, str):
        raise ValueError("Directory path must be a string.")
    
    # Prevent directory traversal attacks
    sanitized_directory = shlex.quote(directory)
    
    # Construct the command using formatted strings
    command = f"ls {sanitized_directory}"
    
    try:
        # Execute the command using subprocess.run()
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr.strip()}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
# Note: This is a simplified example for demonstration purposes. In a real-world scenario, you would implement proper error handling and validation for the directory path.
execute_ls("/path/to/directory")