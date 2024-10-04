import subprocess
import shlex

def execute_command(command, check=True):
    """
    Executes a given command securely using subprocess module.
    
    Args:
        command (str): The command to be executed.
        check (bool): Whether to check the command's return code. Defaults to True.
    
    Returns:
        The command's output as a string.
    """
    try:
        # Securely split the command into arguments
        safe_command = shlex.split(command)
        
        # Execute the command securely using subprocess module
        process = subprocess.Popen(safe_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate()
        
        if check and process.returncode:
            raise subprocess.CalledProcessError(process.returncode, safe_command, output=output, stderr=error)
        
        return output
    except Exception as e:
        # Handle exceptions and errors
        print(f"An error occurred: {e}")
        return str(e)

def main():
    # Example usage
    command = "ls /path/to/directory"
    
    # Ensure the command string is properly formatted with placeholders
    if not isinstance(command, str):
        print("Error: The command must be a string.")
        return
    
    # Securely execute the command
    output = execute_command(command, check=True)
    
    # Print the output securely
    if output:
        print(output.strip())

if __name__ == "__main__":
    main()