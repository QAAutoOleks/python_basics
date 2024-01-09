def how_many_digits_in_number(number):
    count_iterations = 1
    while(abs(number) >= 10):
        number = number / 10
        count_iterations += 1
    return count_iterations

assert how_many_digits_in_number(-20) == 2
assert how_many_digits_in_number(50) == 2
assert how_many_digits_in_number(101.69) == 3
assert how_many_digits_in_number(0) == 1
assert how_many_digits_in_number(1000) == 4