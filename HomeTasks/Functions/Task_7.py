def suma(a, b, c):
    if (a != b) and (b != c):
        print(a + b + c)
    else:
        print(0)


a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

suma(a, b, c)