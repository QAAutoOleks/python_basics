value1 = input("Введіть перший елемент ")
value2 = input("Введіть другий елемент ")
value3 = input("Введіть третій елемент ")
value4 = input("Введіть четвертий елемент ")
value5 = input("Введіть п'ятий елемент ")

# your code goes here
value_tuple_1 = (value1,)
value_tuple_2 = (value2,)
value_tuple_3 = (value3,)
value_tuple_4 = (value4,)
value_tuple_5 = (value5,)
tuple_sum = value_tuple_1 + value_tuple_2 + value_tuple_3 + value_tuple_4 + value_tuple_5
tuple_last_2 = (tuple_sum[3], tuple_sum[4])
print(tuple_last_2)
