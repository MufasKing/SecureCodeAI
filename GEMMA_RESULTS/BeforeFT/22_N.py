import os
import sys

def main():
    filename = sys.argv[1]
    filepath = os.path.join("/safe/", filename)
    with open(filepath, "r") as f:
        for line in f:
            print(line)

if __name__ == "__main__":
    main()