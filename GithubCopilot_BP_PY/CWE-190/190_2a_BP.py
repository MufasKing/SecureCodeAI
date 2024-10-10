import secrets
from decimal import Decimal, InvalidOperation
import logging
import json
from cryptography.fernet import Fernet

# Configure logging
logging.basicConfig(filename='application.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Generate a key for encryption/decryption
# In a real application, you should store this key securely
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def get_secure_random_decimal():
    """Generate a secure random number as a Decimal."""
    random_float = secrets.randbelow(1000000) / 10000.0  # Example: generate a random number
    return Decimal(random_float)

def validate_input(user_input):
    """Validate if the input is a valid Decimal number."""
    try:
        val = Decimal(user_input)
        return True, val
    except InvalidOperation:
        return False, None

def encrypt_data(data):
    """Encrypt data using Fernet symmetric encryption."""
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data

def decrypt_data(encrypted_data):
    """Decrypt data using Fernet symmetric encryption."""
    decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
    return decrypted_data

def main():
    logging.info('Application started')
    try:
        user_input = input("Enter a decimal number: ")
        is_valid, decimal_number = validate_input(user_input)
        if not is_valid:
            raise ValueError("Invalid input. Please enter a valid decimal number.")
        
        logging.info('User input validated successfully')
        
        secure_random_decimal = get_secure_random_decimal()
        result = decimal_number + secure_random_decimal
        print(f"Result after adding secure random decimal: {result}")
        
        # Example of data protection: encrypting the result
        encrypted_result = encrypt_data(str(result))
        print(f"Encrypted result: {encrypted_result}")
        
        # Decrypting for demonstration
        decrypted_result = decrypt_data(encrypted_result)
        print(f"Decrypted result: {decrypted_result}")
        
        logging.info('Operation completed successfully')
    except Exception as e:
        logging.error(f'Error occurred: {e}')
        print("An error occurred. Please try again.")

if __name__ == "__main__":
    main()