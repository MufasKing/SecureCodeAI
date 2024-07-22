import argparse

def main():
    # Define the array
    array = [10, 20, 30, 40, 50]
    
    # Create the parser
    parser = argparse.ArgumentParser(description="Access an array element by index.")
    
    # Add an argument
    parser.add_argument("index", help="Index of the array element to be accessed", type=str)
    
    # Parse the argument
    args = parser.parse_args()
    
    try:
        # Convert argument to integer
        index = int(args.index)
        
        # Check if index is within range
        if 0 <= index < len(array):
            print(array[index])
        else:
            print("invalid input")
    
    except ValueError:
        print("invalid input")

if __name__ == "__main__":
    main()