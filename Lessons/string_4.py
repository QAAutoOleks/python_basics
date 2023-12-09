str1 = "Слава Україні!"

# перевірка наявності символу в рядку
print('Слава' in str1)

sym = str(input("Enter symbol: "))
if sym in str1:
    print("String includes symbol '" + sym + "'")
else:
    print("String doesn't include symbol '" + sym + "'")
