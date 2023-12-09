list1 = []
ind = 0
vid = 0
while len(list1) < 9:
    list1.append(int(input("Enter element: ")))
    if list1[ind] < 0:
        vid += 1
    ind += 1
print(vid)
