number = int(input("Введіть число "))
a= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# your code goes here
ind = 0
for i in a:
    if i == number:
        print("Введене число - існує")
        break
    else:
        ind += 1
if ind == 11:
    print("Введене число - не існує")