import secrets
import hashlib

# Define a function to securely generate random sales values
def get_monthly_sales(month):
    # Generate a secure random token
    token = secrets.token_hex(16)
    
    # Hash the token using SHA-256
    hashed_token = hashlib.sha256(token.encode()).hexdigest()
    
    # Use the hashed token to generate a random sales value
    sales_value = int(hashed_token, 16) % 100000  # Assuming sales values are 5-digit numbers
    
    print(f"Month {month + 1} sales: {sales_value}")
    return sales_value

# Main function
def main():
    # Initialize the total sales to 0
    total_sales = 0
    
    # Iterate over the first quarter (3 months)
    for month in range(3):
        # Get the monthly sales securely
        monthly_sales = get_monthly_sales(month)
        
        # Add the monthly sales to the total
        total_sales += monthly_sales
    
    print(f"
Total sales for the first quarter: {total_sales}")

# Call the main function
if __name__ == "__main__":
    main()