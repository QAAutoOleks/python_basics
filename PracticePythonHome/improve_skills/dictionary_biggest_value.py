dict = {
    'a': 10,
    'b': 50,
    'c': 20,
    'd': 8
}

def find_biggest_value_in_list(dict):
    arr = list()
    for key in dict:
        arr.append(dict.get(key))
        # arr.append(dict[key])
    arr.sort()
    return arr

def find_values_of_dict(arr):
    for i in dict:
        if dict[i] == arr[3] or dict[i] == arr[2]:
            print(i)


find_values_of_dict(find_biggest_value_in_list(dict))