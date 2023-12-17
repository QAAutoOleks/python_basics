def display_student(name, age):
    print(name, age)


# Assign a different name to function using the assignment (=) operator
show_student = display_student
show_student("Pes", 10)

def range_between(first, last):
    list_even = []
    for i in range(first, last + 1):
        if i % 2 == 0:
            list_even.append(i)
    print(list_even)


range_between(4, 30)