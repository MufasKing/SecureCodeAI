# In Python, we use import statements to include modules

# Importing a specific module
import sys

# Importing the entire standard library (Note: This is not a typical practice in Python)
# Standard library modules are available by default, you do not need to explicitly import them all.
# You should import only the specific modules you need.

# Example function to demonstrate the inclusion of modules
def main():
    # Using the print function, which is built-in in Python
    print("Hello, World!")
    
    # Example usage of a function from the sys module
    print("Python version:", sys.version)

if __name__ == "__main__":
    main()
