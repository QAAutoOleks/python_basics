n = int(input("Number: "))
list1 = []
n2 = n
a = 1
while n2 > 9:
    a *= 10
    n2 /= 10
while a > 0:
    list1.append(int(n // a))
    n %= a
    a = a // 10
print(list1)