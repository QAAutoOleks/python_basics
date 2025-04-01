# l1 = [1, 2, 3]
# l2 = [4, 5, 6]

# print(l1 + l2)

def merge(lst1, lst2):
    # Write code here
    merged_list = lst1 + lst2
    merged_list.sort()

    return merged_list

print(merge([1, 3], [2]))