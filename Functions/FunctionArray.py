import random

n = int(input("Enter quantity of elements array: "))
array = [n]
for i in range(n - 1):
    array.insert(i, random.randint(-100, 100))
print(array)

def arrays_elements(array_input):
    odd = 0
    even = 0
    negative = 0
    positive = 0

    for i in range(len(array_input)):
        if array_input[i] < 0:
            negative += 1
        else:
            positive += 1
        if array_input[i] % 2 == 1:
            odd += 1
        else:
            even += 1

    print("Negative =", negative)
    print("Positive =", positive)
    print("Odd =", odd)
    print("Even =", even)

arrays_elements(array)

