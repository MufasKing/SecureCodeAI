import secrets
import hashlib

def get_secure_hash(data):
    """
    Generates a secure hash for the given data using SHA-256.
    This ensures that the function's operation is secure.
    """
    return hashlib.sha256(data.encode()).hexdigest()

def getMonthlySales(month):
    """
    Simulates fetching monthly sales data securely.
    This is a placeholder for the actual logic that would securely fetch or calculate monthly sales.
    The use of secrets.token_hex here simulates secure data access or calculation.
    """
    # Simulating secure data fetching/calculation
    secure_data = secrets.token_hex(16)  # Simulated secure data
    secure_hash = get_secure_hash(secure_data)  # Securely hash the data
    # Placeholder for actual sales data, using hash length as a proxy for sales data
    return len(secure_hash)

def calculate_first_quarter_sales():
    """
    Calculates the total sales for the first quarter securely.
    It iterates through the first three months, securely fetching and summing the sales data.
    """
    total_sales = 0
    for month in range(3):  # Iterates from 0 to 2
        monthly_sales = getMonthlySales(month)
        total_sales += monthly_sales
    return total_sales

# Calculate and print the total sales for the first quarter
first_quarter_sales = calculate_first_quarter_sales()
print(f"Total sales for the first quarter: {first_quarter_sales}")