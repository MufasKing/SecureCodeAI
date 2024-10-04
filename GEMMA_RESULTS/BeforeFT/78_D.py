import os

def main():
    # Create a string that contains the ls command
    ls_command = "ls"

    # Execute the ls command
    os.system(ls_command)

    # Print the output of the ls command
    print(os.popen(ls_command).read())

if __name__ == "__main__":
    main()