def max_two(one, two):
    if one > two:
        return one
    else:
        return two
    
one = int(input("One: "))
two = int(input("Two: "))
three = int(input("Three: "))
four = int(input("Four: "))
five = int(input("Five: "))
six = int(input("Six: "))

max1 = max_two(max_two(one, two), three)
max2 = max_two(max_two(four, five), six)

print(max1 + max2)