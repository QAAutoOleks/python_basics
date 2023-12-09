# set = collection which is unordered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}
dinner_table = utensils.union(dishes)

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# utensils.update(dishes)
# print(utensils.difference(dishes)) - вивести тільки елементи, яких немає в dishes
# print(utensils.intersection(dishes)) - виведе тільки однакові елементи в utensils та dishes

for i in dinner_table:
    print(i)