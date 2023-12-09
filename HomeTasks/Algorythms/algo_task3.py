import math

a = int(input("Введіть довжину першого катету: "))
b = int(input("Введіть довжину другого катету: "))
hypotenuse = math.sqrt(a**2 + b**2)
print("Гіпотенуза =", hypotenuse)