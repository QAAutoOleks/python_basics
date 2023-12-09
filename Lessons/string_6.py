str = str(input("Enter string: "))
str_len = len(str)

number = int(input(f"Enter number for checking. Number have to be less than {str_len} and bigger 0: "))
while number < 0 or number > str_len:
    number = int(input(f"Enter correct number for checking. Number have to be less than {str_len} and bigger 0: "))

print(f"{number} symbol in string is '{str[number - 1]}'")
