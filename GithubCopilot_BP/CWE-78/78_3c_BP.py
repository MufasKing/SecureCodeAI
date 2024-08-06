import os

import shlex

import subprocess



def secure_ls_command(directory):

    # Input Validation

    if not isinstance(directory, str):

        raise ValueError("Directory path must be a string.")

    

    # Input Sanitization

    sanitized_directory = shlex.quote(directory)

    

    # Secure Command Execution

    command = f"ls {sanitized_directory}"

    try:

        # Using subprocess.run instead of os.system for better security and control

        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)

        print(f"Contents of {directory}:{result.stdout}")

    except subprocess.CalledProcessError as e:

        print(f"An error occurred while trying to list the contents of {directory}: {e}")

    except Exception as e:

        print(f"An unexpected error occurred: {e}")



# Example usage

directory = "/path/to/directory"

secure_ls_command(directory)