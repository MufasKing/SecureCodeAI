import secrets
import hashlib

def get_monthly_sales(month: int) -> int:
    """
    Simulate the monthly sales for a given month using a secure random number.
    """
    # Generate a secure random sales figure between 1000 and 5000 for demonstration purposes
    sales = secrets.randbelow(4001) + 1000
    return sales

def calculate_first_quarter_sales() -> int:
    """
    Calculate the total sales for the first quarter.
    """
    total_sales = 0
    for i in range(3):
        monthly_sales = get_monthly_sales(i)
        total_sales += monthly_sales
    return total_sales

def main():
    """
    Main function to execute the sales calculation.
    """
    first_quarter_sales = calculate_first_quarter_sales()
    print(f"Total sales for the first quarter: {first_quarter_sales}")

if __name__ == "__main__":
    main()