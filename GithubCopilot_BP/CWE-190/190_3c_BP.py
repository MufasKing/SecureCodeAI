import secrets

def main():
    # Secure Execution and Input Validation
    try:
        # Initialize totalSales variable
        totalSales = 0

        # Assuming sales data is securely fetched or inputted, using secrets for demonstration
        jan_sales = secrets.randbelow(10000)  # Example sales for January
        feb_sales = secrets.randbelow(10000)  # Example sales for February
        mar_sales = secrets.randbelow(10000)  # Example sales for March

        # Add each month's sales to totalSales
        totalSales += jan_sales
        totalSales += feb_sales
        totalSales += mar_sales

        # Print the total sales using f-string for formatting
        print(f"Total Sales: {totalSales}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()