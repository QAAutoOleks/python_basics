first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
sum = 0
index = 0

if first_number < second_number:
    for i in range(first_number, second_number + 1):
        sum += i
        index += 1
        print(sum)
        print(sum / index)
else:
    for i in range(second_number, first_number + 1):
        sum += i
        index += 1
        print(sum)
        print(sum / index)