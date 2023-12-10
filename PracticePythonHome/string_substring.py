# [start:stop:step]

name = "Bro Code"
first_name = name[0:5] # індекс №5 не додається до нової змінної
second_name = name[0:5:1] # те ж саме, що і попередній запис, тому що крок - 1
third_name = name[0:8] # виведеться до 7 символа включно, тобто все слово
fourth_name = name[4:] # виведе всі символи від 4 індекса і до кінця
fifth_name = name[:5] # виведе всі символи від 0 індекса і до 5
sixth_name = name[::-1] # реверс рядка
seventh_name = name[-1]  # останній символ рядка, те ж саме, що і [1], тільки з кінця

print(first_name)
print(second_name)
print(third_name)
print(fourth_name)
print(fifth_name)
print(sixth_name)
print(seventh_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"
# slice = slice(7) виведе все до 7 індекса
# slice = slice(7, 17) виведе все від 7 індекса до 16 включно
# slice = slice(50:) виведе порожній список
psina = slice(7, -4) # виведе все від 7 індекса до 4 з кінця
print(website1[psina])
print(website2[psina])