first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

if first_number < second_number:
    for i in range(first_number, second_number + 1):
        print(i)
else:
    for i in range(second_number, first_number + 1):
        print(i)