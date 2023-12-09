list1 = []
max = 0
ind = 0
while len(list1) < 10:
    list1.append(int(input("Enter element: ")))
    if ind % 2 != 0 and list1[ind] % 3 == 0 and list1[ind] > max:
        max = list1[ind]
    ind += 1
print(max)