import secrets
import string

def generate_random_sales():
    """
    Generates a random sales figure between 0 and 100,000.
    """
    return secrets.randbelow(100001)

def validate_month(month_str):
    """
    Validates the input month string.
    Returns the month number if valid, otherwise raises a ValueError.
    """
    valid_months = {month.lower(): index + 1 for index, month in enumerate(string.capwords(', '.join([m[:3] for m in ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])).split(', '))}

    if month_str.lower() not in valid_months:
        raise ValueError(f"Invalid month '{month_str}'. Please enter a valid month (e.g., Jan, February).")

    return valid_months[month_str.lower()]

def get_monthly_sales(month):
    """
    Generates and returns the monthly sales for a given month.
    """
    return generate_random_sales()

def print_quarterly_sales(quarterly_sales):
    """
    Prints the quarterly sales figures.
    """
    for quarter, sales in enumerate(quarterly_sales, start=1):
        print(f"Quarter {quarter} sales: {sales}")

def main():
    """
    Main function to get monthly sales and print quarterly sales.
    """
    quarterly_sales = [0, 0, 0, 0]

    for _ in range(12):
        try:
            month_number = validate_month(input("Enter a month (e.g., Jan, February): "))
        except ValueError as e:
            print(e)
            continue

        quarter_index = (month_number - 1) // 3
        quarterly_sales[quarter_index] += get_monthly_sales(month_number)

    print_quarterly_sales(quarterly_sales)

if __name__ == "__main__":
    main()