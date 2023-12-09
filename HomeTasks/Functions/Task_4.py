def max_two(one, two):
    if one > two:
        return one
    else:
        return two


number1 = int(input("Number1: "))
number2 = int(input("Number2: "))
number3 = int(input("Number3: "))
number4 = int(input("Number4: "))


max1 = max_two(number1, number2)
max2 = max_two(number3, number4)
max = max_two(max1, max2)
print(max)
