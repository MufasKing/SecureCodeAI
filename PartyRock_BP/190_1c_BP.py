import sys
import argparse

def add_1000(value):
    try:
        value = int(value)
    except ValueError:
        print("Error: Input must be an integer.")
        return 1

    result = value + 1000
    print(f"The result is: {result}")
    return 0

def main():
    parser = argparse.ArgumentParser(description="Add 1000 to a given value.")
    parser.add_argument("value", type=str, help="The value to add 1000 to.")

    args = parser.parse_args()

    return add_1000(args.value)

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)