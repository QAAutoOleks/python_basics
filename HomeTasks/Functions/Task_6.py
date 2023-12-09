def triangle_check(a, b, c):
    if ((a + b) > c) and ((b + c) > a) and ((a + c) > b):
        print("Трикутник існує")
    else:
        print("Трикутник не існує")


a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

triangle_check(a, b, c)