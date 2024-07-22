import random
import secrets

def generate_secure_random_float():
    """Generates a secure random float between 0 and 1."""
    try:
        random_float = secrets.SystemRandom().uniform(0, 1)
        if not (0 <= random_float <= 1):
            raise ValueError("Generated float is out of bounds.")
        return random_float
    except Exception as e:
        raise ValueError(f"Error generating secure random float: {e}")

def convert_float_to_string(value):
    """Converts a float to a string with secure handling."""
    try:
        if not isinstance(value, float):
            raise TypeError("Input value is not a float.")
        return f"{value:.10f}"
    except Exception as e:
        raise ValueError(f"Error converting float to string: {e}")

def main():
    try:
        # Generate secure random floats
        float_a = generate_secure_random_float()
        float_b = generate_secure_random_float()
        float_c = generate_secure_random_float()
        
        # Convert floats to strings
        str_a = convert_float_to_string(float_a)
        str_b = convert_float_to_string(float_b)
        str_c = convert_float_to_string(float_c)
        
        # Print results
        print("Secure random floats converted to strings:")
        print("str_a:", str_a)
        print("str_b:", str_b)
        print("str_c:", str_c)
        
    except ValueError as ve:
        print(ve)

if __name__ == "__main__":
    main()