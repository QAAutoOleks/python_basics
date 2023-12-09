list1 = []
ind = 0
dobutok = 1
while len(list1) < 7:
    list1.append(float(input("Enter element: ")))
    if list1[ind] > 0:
        dobutok *= list1[ind]
    ind += 1
print(dobutok)