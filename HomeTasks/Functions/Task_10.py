def gsd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return gsd(num2, num1 % num2)
    

a = int(input("a: "))
b = int(input("b: "))

print(gsd(a, b))