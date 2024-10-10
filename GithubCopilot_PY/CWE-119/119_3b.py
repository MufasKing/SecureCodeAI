import sys

def atoi(s):
    try:
        return int(s)
    except ValueError:
        return None

def main():
    argc = len(sys.argv)
    argv = sys.argv

    print(f"Number of arguments (argc): {argc}")
    for i, arg in enumerate(argv):
        print(f"Argument {i}: {arg}")

    # Example usage of atoi
    if argc > 1:
        for i in range(1, argc):
            converted = atoi(argv[i])
            if converted is not None:
                print(f"Converted '{argv[i]}' to integer: {converted}")
            else:
                print(f"Could not convert '{argv[i]}' to integer")

if __name__ == "__main__":
    main()