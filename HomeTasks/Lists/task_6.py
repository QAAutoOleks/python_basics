list1 = []
while len(list1) < 8:
    list1.append(float(input("Enter element: ")))
max = list1[0]
min = list1[0]
ind = 0
imax = 0
imin = 0
for i in list1:
    if i > max:
        max = i
        imax = ind
    if i < min:
        min < i
        imin = ind
    ind += 1
print(list1)
list1[imax], list1[imin] = list1[imin], list1[imax]
# list1[imin] = max 
# list1[imax] = min
print(list1)