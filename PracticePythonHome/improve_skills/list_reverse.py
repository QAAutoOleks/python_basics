def reverse(lst):
    # Write code here
    lst_reverse = []
    for i in range(len(lst), 0, -1):
        lst_reverse.append(lst[i-1])
    return lst_reverse

print(reverse([1, 2, 3]))