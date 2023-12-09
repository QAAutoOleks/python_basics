number1 = int(input("Введіть перше ціле число: "))
number2 = int(input("Введіть друге ціле число: "))

sum = number1 + number2
sum1 = pow(number1, 2) + pow(number2, 2)  # number1**2 + number2**2
sum2 = pow((number1 + number2), 2)

print(sum)
print(sum1)
print(sum2)