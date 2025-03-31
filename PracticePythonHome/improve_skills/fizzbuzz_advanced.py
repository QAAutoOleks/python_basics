print('Welcome to FizzBuzz!')

def fizzbuzz(number):
    almost = False
    for i in range(number+1):
        if i == 0:
            pass
        elif i % 3 == 0 and i % 7 == 0:
            print("FizzBuzz")
        elif i % 3 == 0 and i % 7 != 0:
            print("Fizz")
        elif i % 7 == 0 and i % 3 != 0:
            print("Buzz")
        else:
            for j in str(i):
                if j == '3':
                    almost = True
                    break
                else:
                    pass
            if almost:
                print('Almost Fizz')
                almost = False
            else:
                print(str(i))

user_number = int(input())
fizzbuzz(user_number)