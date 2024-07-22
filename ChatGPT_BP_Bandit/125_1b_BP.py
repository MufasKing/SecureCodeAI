import sys

def getValueFromArray(arr, size, index):
    if index >= 0 and index < size:
        return arr[index]
    else:
        return -1

def main():
    try:
        # Read the input integer
        input_integer = int(input().strip())
        
        # Define your array
        id_sequence = [1, 3, 5, 7, 9]  # Example array
        
        # Get the size of the array
        size_of_array = len(id_sequence)
        
        # Call getValueFromArray with the array, its size, and the input integer
        result = getValueFromArray(id_sequence, size_of_array, input_integer)
        
        # Return the result as the exit code
        sys.exit(result)
        
    except ValueError:
        print("Error: Input must be a valid integer.")
        sys.exit(1)
    except IndexError:
        print("Error: Index out of bounds.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()