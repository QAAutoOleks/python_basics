first = int(input("First = "))
second = int(input("Second = "))
multiple = int(input("Enter multiple = "))

while first <= second:
    if first % multiple == 0:
        print(first)
    first += 1