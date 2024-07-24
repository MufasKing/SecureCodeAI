import secrets

def main():
    # Initialize totalSales variable
    totalSales = 0.0
    
    # Add sales for each month to totalSales
    for month in ["January", "February", "March"]:
        sales = input(f"Enter the sales for {month}: ")
        if is_valid_sales_input(sales):
            totalSales += float(sales)
        else:
            print(f"Invalid input for {month}. Sales must be a positive number.")
            return

    # Generate a secret key using secrets module for security (e.g., for encryption/authentication)
    secret_key = secrets.token_hex(16)
    print(f"Secret Key (for security purposes): {secret_key}")

    # Print the total sales to the screen
    print(f"The total sales for the first quarter are: ${totalSales:.2f}")

def is_valid_sales_input(sales):
    """
    Validates the sales input ensuring it's a positive number.
    """
    try:
        value = float(sales)
        if value < 0:
            return False
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    main()