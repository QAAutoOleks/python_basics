list1 = [100, 200, 300, 400, 500]
list2 = list1[::-1]
list1.reverse()
print(list1)
print(list2)

list1 = ["M", "na", "i", "Ke"] 
# If one tuple contains more items, these items are ignored
list2 = ["y", "me", "s", "lly", "!!!"]
list3 = [i + j for i, j in zip(list1, list2)]
list4 = [i + j for i, j in zip(list2, list1)]
print(list3)
print(list4)

numbers = [1, 2, 3, 4, 5, 6, 7]
numbers_output = []
for i in numbers:
    numbers_output.append(i**2)
print(numbers_output)

# or use list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7]
res = [x * x for x in numbers]
res2 = [str(x) for x in numbers]
print(res)
print(res2)

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = []
for i in list1:
    list3.append(i + list2[0])
    list3.append(i + list2[1])
print(list3)

# or use list comprehension
res = [x + y for x in list1 for y in list2]
print(res)