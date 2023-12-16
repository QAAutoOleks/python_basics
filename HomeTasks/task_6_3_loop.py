number = int(input("Введіть число"))

# your code goes here
a = 0
while number >= 0:
    if a % 2 == 0:
        print(a**2)
    else:
        print(a)
    a += 1
    number -= 1