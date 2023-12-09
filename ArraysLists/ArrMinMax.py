import random

array = [10]
negative = 0
positive = 0
zero = 0

for i in range(0, 9):
    array.insert(i, random.randint(-100, 100))
    if array[i] < 0:
        negative += 1
    elif array[i] > 0:
        positive += 1
    else:
        zero += 1

print(array)
print("Negative =", negative)
print("Positive =", positive)
print("Zero =", zero)
print("Max =", max(array))
print("Min =", min(array))
print("Reverse =", array[::-1])