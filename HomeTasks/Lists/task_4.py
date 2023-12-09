list1 = []
ind = 0
while len(list1) < 6:
    list1.append(float(input("Enter element: ")))
max = list1[0]
for i in list1:
    if i > max:
        max = i
print(max)

