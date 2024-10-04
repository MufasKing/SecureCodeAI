import sys

# Define the array
array = [10, 20, 30, 40, 50]

# Function to validate and process the input
def process_input(user_input):
    try:
        # Convert the input to an integer
        index = int(user_input)
        
        # Validate the index
        if index >= 0 and index < len(array):
            # Return the element at the valid index
            return array[index]
        else:
            # Return -1 for invalid index
            return -1
    except ValueError:
        # Handle non-integer inputs
        print("Error: Please enter a valid integer.")
        return -1
    except IndexError:
        # Handle out-of-bounds indices
        print("Error: Index out of bounds.")
        return -1
    except Exception as e:
        # Handle any other exceptions
        print(f"Error: {str(e)}")
        return -1

# Main function to handle user input
def main():
    try:
        # Get user input
        user_input = input("Enter an index: ")
        
        # Process the input
        result = process_input(user_input)
        
        # Print the result
        if result == -1:
            print("Result: -1")
        else:
            print(f"Result: {result}")
    except Exception as e:
        # Handle any exceptions from main function
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()