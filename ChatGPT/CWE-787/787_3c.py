import sys

def main():
    # Check if there is at least one command line argument
    if len(sys.argv) < 2:
        print("Usage: python script.py <argument>")
        sys.exit(1)
    
    # Get the command line argument (first argument after the script name)
    argument = sys.argv[1]
    
    # Trim any trailing whitespace characters
    trimmed_argument = argument.rstrip()
    
    # Print the trimmed argument
    print(trimmed_argument)

if __name__ == "__main__":
    main()
