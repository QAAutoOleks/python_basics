n = int(input("Number: "))
n2 = n
a = 1
while n2 > 9:
    a *= 10
    n2 /= 10
while a > 0:
    print(int(n // a))
    n %= a
    a = a // 10