str1 = "Слава Україні!"
str2 = "Сузір'я"
str3 = """Всередині потрійних можна використовувати
як 'одинарні' так "подвійні" лапки"""
str4 = str(1) # перетворення до типу str

number = int(input("Enter number for checking. Number have to be less than 13 and bigger 0:"))
while number < 0 or number > 13:
    print("Enter correct number:")
    number = int(input("Enter number for checking. Number have to be less than 13 and bigger 0:"))

if str1[number] == 'С':
    print("Symbol with index '" + str(number) + "' is 'C'")
else:
    print("Symbol with index '" + str(number) + "' is not 'C'")