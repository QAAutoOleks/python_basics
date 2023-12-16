number = int(input("Введіть число"))

# your code goes here
def is_even_or_odd(number):
    if number % 2 == 0:
        res = "число " + str(number) + " парне"
    else:
        res = "число " + str(number) + " непарне"
    return res
print(is_even_or_odd(number))
  