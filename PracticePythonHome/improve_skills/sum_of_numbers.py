def sum_of_number(number):
    sum = 0
    for i in range(1, number + 1):
        sum += i
    return sum


print(sum_of_number(10))