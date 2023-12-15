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
print(add, sub)


# variable length
def func(*args):
    for i in args:
        print(i)


func(20, 40, 100)