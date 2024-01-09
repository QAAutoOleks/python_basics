def how_many_digits_in_number(number):
    number1 = number
    number2 = number
    count_iterations = 1
    while(abs(number1) >= 10):
        number1 = number1 / 10
        count_iterations += 1
    while(isinstance(number2, float)):
        if number2 % 10 == 0:
            count_iterations -= 1
            break
        count_iterations += 1
        number2 *= 10
    return count_iterations
    

assert how_many_digits_in_number(-20) == 2
assert how_many_digits_in_number(50) == 2
assert how_many_digits_in_number(101.69) == 5
assert how_many_digits_in_number(0) == 1
assert how_many_digits_in_number(1000) == 4
assert how_many_digits_in_number(-10165.697) == 8