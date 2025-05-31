lst = [80, 4, 99, 36, 34]
output_list = []
for index, number in enumerate(lst):
    if number < 50 or number % 5 == 0:
        output_list.append(index)

print(output_list)