list1 = []
list1.append(int(input("Enter first element: ")))
dif = int(input("Enter difference: "))
sum = list1[0]
for i in range(9):
    list1.append(list1[i] + dif)
    sum += list1[i + 1]
print(list1)
print(sum)