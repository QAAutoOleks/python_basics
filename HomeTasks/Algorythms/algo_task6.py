import math

a = int(input("Перша сторона: "))
b = int(input("Друга сторона: "))
alfa = int(input("Кут: "))

s = a * b * math.sin(alfa) / 2
print(s)