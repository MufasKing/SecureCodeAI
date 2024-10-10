import secrets
import string

def validate_month(month):
    """Validate the month input."""
    if month not in range(1, 13):
        raise ValueError("Invalid month. Month must be between 1 and 12.")

def get_monthly_sales():
    """Generate a random monthly sales figure."""
    return secrets.randbelow(100001)  # Generates a random number between 0 and 100000

def calculate_quarterly_sales():
    """Calculate and print the quarterly sales."""
    quarterly_sales = [0, 0, 0, 0]  # Initialize quarterly sales
    
    for month in range(1, 13):
        validate_month(month)  # Validate the month
        sales = get_monthly_sales()  # Get the sales for the month
        
        # Determine the quarter for the current month and add the sales to the appropriate quarter
        if month <= 3:
            quarterly_sales[0] += sales
        elif month <= 6:
            quarterly_sales[1] += sales
        elif month <= 9:
            quarterly_sales[2] += sales
        else:
            quarterly_sales[3] += sales
    
    # Print the quarterly sales
    for i, sales in enumerate(quarterly_sales, start=1):
        print(f"Q{i} sales: {sales}")

# Call the function to calculate and print the quarterly sales
calculate_quarterly_sales()