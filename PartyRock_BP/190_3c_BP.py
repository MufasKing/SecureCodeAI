import secrets
import re

def main():
    # Validate user input for sales
    def validate_sales(sales_input):
        if not re.match(r'^[0-9]+(\.[0-9]+)?$', sales_input):
            raise ValueError("Invalid input. Please enter a valid number.")
        return float(sales_input)

    # Generate a secure random token
    token = secrets.token_urlsafe(16)

    # Initialize total sales
    total_sales = 0.0

    # Get sales for each month with input validation
    try:
        jan_sales = validate_sales(input(f"Enter sales for January ({token}): "))
        feb_sales = validate_sales(input(f"Enter sales for February ({token}): "))
        mar_sales = validate_sales(input(f"Enter sales for March ({token}): "))
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Calculate total sales
    total_sales = jan_sales + feb_sales + mar_sales

    # Print total sales
    print(f"Total sales: {total_sales:.2f}")

if __name__ == "__main__":
    main()