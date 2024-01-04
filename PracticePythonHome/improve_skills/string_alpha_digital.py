def count_symbols(given_string):
    alpha = 0
    digital = 0
    char = 0
    for i in given_string:
        if i.isalpha():
            alpha += 1
        elif i.isdigit():
            digital += 1
        else:
            char += 1
    print(f"Chars: {alpha}\nDigits: {digital}\nSymbol: {char}")

count_symbols("P@#yn26at^&i5ve")
