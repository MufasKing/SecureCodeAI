import random

vehicles = ["car", "truck", "boat", "airplane"]

index = random.randint(0, len(vehicles) - 1)

print("The vehicle at index " + str(index) + " is " + vehicles[index] + ".")

for vehicle in vehicles:
    print(vehicle)