import secrets
import string

# Function to generate monthly sales
def getMonthlySales():
    return secrets.randbelow(100001)  # Generates a random number from 0 to 100000

# Main function to compute quarterly totals and print results
def main():
    quarters = [[], [], [], []]  # List to hold sales for each quarter

    # Generate sales for each month
    for month in range(1, 13):
        sales = getMonthlySales()
        quarter_index = (month - 1) // 3  # Determine the quarter index (0-3)
        quarters[quarter_index].append(sales)  # Add sales to corresponding quarter

    # Calculate quarterly totals and print results
    for i, quarter in enumerate(quarters):
        quarter_total = sum(quarter)
        quarter_name = f"Q{i+1}"  # Quarter name (e.g., Q1, Q2, ...)
        print(f"Total sales for {quarter_name}: ${quarter_total:,}")  # Format with commas

if __name__ == "__main__":
    main()
