n = int(input("n: "))
for i in range(n, -1, -1):
    print(i, end=" ")
    for j in range (0, i):
        print("#", end=" ")
    print()