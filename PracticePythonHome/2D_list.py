# 2D lists = a list of lists

drinks = ["coffee", "soda", "hotdog"]
dinner = ["pizza", "humburger", "hotdog"]
dessert = ["cake", "ice-cream"]

food = [drinks, dinner, dessert]

print(food)
print(food[0][0])

rows, cols = (5, 3)
print([[0 for i in range(cols)] for j in range(rows)])


#Create 2D array with 4 rows and 5 columns
#array=[[23,45,43,23,45],[45,67,54,32,45],[89,90,87,65,44],[23,45,67,32,10]]
#insert the row at 5 th position
#array.insert(2, [1,2,3,4,5])
#insert the row at 6 th position
#array.insert(2, [1,2,3,4,5])
#insert the row at 7 th position
#array.insert(2, [1,2,3,4,5])
#Output
#[[23, 45, 43, 23, 45], [45, 67, 54, 32, 45], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 
# [1, 2, 3, 4, 5], [89, 90, 87, 65, 44], [23, 45, 67, 32, 10]]


# Nested List Comprehensions
array = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(array)

# Output:
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

s = "ZXCVBN"
#                          в цьому циклі буде
#    виводиться кожний     6 ітерацій, тому що
#      символ рядка "s"    "ZXCVBN" - 6 символів   буде 2 рядка
array = [[s[j] for j in range(0, len(s))] for i in range(1, 3)]
print(array)