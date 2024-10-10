import subprocess

import shlex



def execute_command(command):

    """
    
    Executes a given command securely using subprocess module.

    

    Args:

    - command (str): The command to be executed.

    

    Returns:

    - output (str): The output of the executed command.

    - error (str): The error message if command execution fails.

    """

    try:

        # Securely parse the command to avoid shell injection vulnerabilities

        safe_command = shlex.split(command)

        

        # Execute the command without opening a shell

        process = subprocess.Popen(safe_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        output, error = process.communicate()

        

        if process.returncode == 0:

            return output, None

        else:

            return None, error

    except Exception as e:

        return None, str(e)



def main():

    # Example usage

    directory = "/path/to/directory"

    

    # Input validation and sanitization

    if not isinstance(directory, str):

        print("Error: Directory path must be a string.")

        return

    

    # Replace potentially dangerous characters or sequences

    sanitized_directory = directory.replace(";", "").replace("&", "").replace("`", "")

    

    # Construct the command string securely

    command = f"ls {shlex.quote(sanitized_directory)}"

    

    # Execute the command

    output, error = execute_command(command)

    

    if error:

        print(f"Error executing command: {error}")

    else:

        print(f"Command output:{output}")



if __name__ == "__main__":

    main()