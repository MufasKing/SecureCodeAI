import sys

def main():
    if len(sys.argv) > 1:
        argument = sys.argv[1].rstrip()
        print(argument)
    else:
        print("Usage: python 787_3c.py <argument>")

if __name__ == "__main__":
    main()