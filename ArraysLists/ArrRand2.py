import random

n = int(input("Enter quantity of elements array: "))
a = [n]

for i in range(n - 1):
    a.insert(i, random.randint(1, 10))
print(a)