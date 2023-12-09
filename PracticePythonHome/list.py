food = ["pizza", "humburger", "hotdog", "spagetti"]

food[3] = "sushi" # new value to index 3

print(food) # весь лист
print(food[0]) # 0 індекс

for x in food:
    print(x)

food.append("ice-cream") # add new element to the end
food.remove("hotdog") # delete hotdog
food.pop() # remove last element
food.insert(0, "cake") # add cake to index 0
food.sort() # sort a-b
food.clear() # delete all values