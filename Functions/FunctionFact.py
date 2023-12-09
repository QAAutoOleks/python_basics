import random

array = [random.randint(1, 5) for x in range(10)]
print(array)

def factorial(array_input):
    array2 = []
    var = 1
    for x in range(len(array_input)):
        for i in range(1, array_input[x] + 1):
            var *= i
        array2.append(var)
        var = 1
    print(array2)
factorial(array)