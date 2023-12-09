n = int(input("Enter quantity dyscyplin: "))
avg = 0
for i in range(0, n):
    print("Mark for", i+1, "dyscyplin: ", end="")
    mark = int(input(""))
    avg += mark
print("Average =", avg / n)