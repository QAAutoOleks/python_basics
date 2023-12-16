def hello(first_name, last_name, age):
    print("Hello " + first_name + " " + last_name)
    print("You are " + str(age) + " years old")
    print("Have a nice day!")


hello("Bro", "Code", 21)


# return multiple values from a function
def calculation(a, b):
    # addiction = a + b
    # substraction = a - b
    # return addiction, substraction
    return a + b, a - b


# return 'tuple'
# print(calculation(20, 15))
add, sub = calculation(40, 10)
print()
print(add, sub)


# variable length
def func(*args):
    for i in args:
        print(i)


print()
func(20, 40, 100)


def showEmployee(name, salary=9000):
    print(f"Name: {name}\nSalary: {salary}")


print()
showEmployee("Ben", 12000)
showEmployee("Jessa")
