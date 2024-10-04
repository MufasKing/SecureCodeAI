import random

items = ["apple", "banana", "orange", "pear", "grape"]

index = int(input("Enter the index of an item: "))

item = items[index]

print("The item at index", index, "is", item)

for item in items:
    print(item)