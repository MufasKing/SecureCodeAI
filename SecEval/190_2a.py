import random
import decimal

def generate_large_random_number():
  return random.randint(1001, 10000)

def main():
  num1 = generate_large_random_number()
  num2 = generate_large_random_number()
  num3 = generate_large_random_number()
  total = decimal.Decimal(num1) + decimal.Decimal(num2) + decimal.Decimal(num3)
  print(total)

if __name__ == '__main__':
  main()