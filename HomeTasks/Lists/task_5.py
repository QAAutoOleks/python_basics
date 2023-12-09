list1 = []
while len(list1) < 12:
    list1.append(float(input("Enter element: ")))
max = list1[0]
for i in list1:
    if i > max:
        max = i
for i in list1:
    if i >= max * 0.7:
        print(i)