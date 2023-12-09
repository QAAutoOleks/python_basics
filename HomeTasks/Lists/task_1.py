list1 = []
sum = 0
while len(list1) < 10:
    list1.append(int(input("Enter element: ")))
print(list1)
for i in list1:
    sum += i
print(sum)