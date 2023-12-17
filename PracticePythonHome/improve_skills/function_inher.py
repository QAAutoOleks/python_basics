def display_student(name, age):
    print(name, age, "\n")


# Assign a different name to function using the assignment (=) operator
show_student = display_student
show_student("Pes", 10)

def range_between(first, last):
    list_even = []
    for i in range(first, last + 1):
        if i % 2 == 0:
            list_even.append(i)
    return list_even


print(f"Range: {range_between(4, 30)}\n")


def largest_item(given_list):
    # given_list.sort()
    # return given_list[len(given_list) - 1]
    return max(given_list)


x = [4, 6, 8, 24, 12, 2]
print(f"Largest item: {largest_item(x)}")