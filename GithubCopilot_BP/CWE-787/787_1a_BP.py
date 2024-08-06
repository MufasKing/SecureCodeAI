import secrets
import string

def get_secure_random_float():
    """
    Generates a secure random float between 0 and 1 using secrets module.
    """
    secure_random_int = secrets.randbits(64)
    secure_random_float = secure_random_int / (2**64)
    return secure_random_float

def validate_input(input_str):
    """
    Validates if the input string contains only digits, a dot, or a minus sign.
    """
    allowed_chars = string.digits + ".-"
    return all(char in allowed_chars for char in input_str)

def secure_str_convert(float_value):
    """
    Converts a float to a string securely and validates the resulting string.
    """
    try:
        secure_str = str(float_value)
        if validate_input(secure_str):
            return secure_str
        else:
            raise ValueError("Invalid characters in the resulting string")
    except ValueError as e:
        print(f"Error: {e}")
        return None

def main():
    try:
        # Generate three random floats
        random_float_a = get_secure_random_float()
        random_float_b = get_secure_random_float()
        random_float_c = get_secure_random_float()

        # Convert them to secure strings
        str_a = secure_str_convert(random_float_a)
        str_b = secure_str_convert(random_float_b)
        str_c = secure_str_convert(random_float_c)

        if str_a and str_b and str_c:
            print(f"str_a: {str_a}")
            print(f"str_b: {str_b}")
            print(f"str_c: {str_c}")
        else:
            print("Error: Failed to generate secure strings")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()