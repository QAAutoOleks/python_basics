a = int(input("First: "))
b = int(input("Second: "))
c = int(input("Third: "))
count = 0
if a == b and a == c:
    count = 2
elif a == b or a == c or b == c:
    count = 1
print(count)