import random

list1 = []
list2 = []

for i in range(10):
    list1.append(random.randint(1, 10))
    list2.append(random.randint(1, 10))

for i in range(10):
    list2[i] = list1[i]

for i in range(10):
    print(list2[i])