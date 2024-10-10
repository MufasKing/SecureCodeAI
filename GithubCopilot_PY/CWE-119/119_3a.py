import sys

def atoi(s):
    return int(s)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python 119_3a.py <index> <arg1> <arg2> ...")
        sys.exit(1)
    
    index = atoi(sys.argv[1])
    if index < 2 or index >= len(sys.argv):
        print("Index out of range")
        sys.exit(1)
    
    print(sys.argv[index])
    sys.exit(0)