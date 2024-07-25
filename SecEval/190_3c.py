import sys
import random

def main():
  # Declare a variable to store total sales
  totalSales = 0

  # Add the sales for each month to totalSales
  totalSales += getMonthlySales(1)
  totalSales += getMonthlySales(2)
  totalSales += getMonthlySales(3)

  # Check if totalSales exceeds the maximum size of an integer
  if totalSales > sys.maxsize:
    print("Error: Number too big.")
    exit()

  # Print the total sales to the screen
  print("Total sales:", totalSales)

def getMonthlySales(month):
  # Returns a random number between 0 and 100000
  return random.randint(0, 100000)

main()