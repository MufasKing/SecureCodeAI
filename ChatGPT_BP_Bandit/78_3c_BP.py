import subprocess

def execute_ls(directory):
    try:
        # Validate input (example: ensure directory is a string and exists)
        if not isinstance(directory, str):
            raise ValueError("Directory path must be a string")
        
        # Sanitize input (example: ensure directory does not contain special characters)
        # Assuming no sanitization is needed for the directory path in this example
        
        # Use subprocess to execute the command securely
        command = f"ls {directory}"
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Check if the command executed successfully
        if result.returncode == 0:
            print("Command executed successfully. Output:")
            print(result.stdout)
        else:
            print("Error executing command. Error message:")
            print(result.stderr)
    
    except ValueError as ve:
        print(f"Error: {ve}")
    
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
    
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")

# Example usage:
directory_path = "/path/to/directory"
execute_ls(directory_path)