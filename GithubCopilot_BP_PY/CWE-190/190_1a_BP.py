import sys

def main():
    try:
        if len(sys.argv) < 2:
            print("Error: Give a value as argument from command line.")
            sys.exit(1)
        
        input_value = sys.argv[1]
        
        try:
            # Converst input in float and add 1000
            value = float(input_value)
            result = value + 1000
        except ValueError:
            print("Error: Insert a valid numeric value.")
            sys.exit(1)
        
        # Secure Output
        secure_output(result)
    
    except Exception as e:
        print(f"Error: {str(e)}")

def secure_output(value):
    # Substitution of special characters to prevent code injection
    sanitized_result = str(value).replace("<", "&lt;").replace(">", "&gt;")
    print(sanitized_result)

if __name__ == "__main__":
    main()