rows = int(input("How many rows?: "))
colums = int(input("How many colums?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(colums):
        print(symbol, end=" ") # символ не переноситься на новий рядок
    print()