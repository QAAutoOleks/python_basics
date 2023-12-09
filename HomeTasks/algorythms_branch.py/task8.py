num1 = int(input("Num1: "))
num2 = int(input("Num2: "))
sum = num1 + num2
product = num1 * num2
if product > sum:
    print("Добуток =", product)
elif product < sum:
    print("Сума =", sum)
else:
    print(num1 - num2)