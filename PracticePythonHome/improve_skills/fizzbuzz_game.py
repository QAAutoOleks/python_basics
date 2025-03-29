print('Welcome to FizzBuzz!')

def fizzbuzz(number):
    for i in range(number+1):
        if i % 3 == 0 and i % 7 == 0:
            print("FizzBuzz")
        elif i % 3 == 0 and i % 7 != 0:
            print("Fizz")
        elif i % 7 == 0 and i % 3 != 0:
            print("Buzz")
        else:
            print(int(i))

user_number = int(input())
fizzbuzz(user_number)