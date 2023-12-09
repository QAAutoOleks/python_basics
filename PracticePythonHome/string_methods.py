name = "Bro"
name_digit = "123"
name_not_alpha = "Bro Bro Bobr Bobr"
print(len(name)) # довжина значення у змінній
print(name.find("B")) # пошук індексу символу "В"
print(name.capitalize()) # збільшує ТІЛЬКИ першу літеру
print(name.upper()) # збільшує ВСІ літери
print(name.lower()) # зменшує ВСІ літери
print(name_digit.isdigit()) # чи складається значення з чисел
print(name.isdigit()) # чи складається значення з чисел
print(name.isalpha()) # чи складається значення тільки з латинських літер. 
# Пробіл - не латинська літера
print(name_not_alpha.isalpha()) # False
print(name.count("r")) # рахує кількість певних символів (напр. "r")
print(name_not_alpha.count("r"))
print(name_not_alpha.replace("r", "Y")) # змінює всі певні літери на інші
print(name_not_alpha.replace(" ", "")) # видалити пробіли
print(name_not_alpha*3) # вивести значення 3 рази