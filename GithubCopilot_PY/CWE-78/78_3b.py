import os

def execute_command(command):
    os.system(command)

directory = "."

# Using the print function to create the command string
command_string = "ls {}".format(directory)
execute_command(command_string)