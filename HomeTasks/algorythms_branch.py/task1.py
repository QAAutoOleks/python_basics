day = int(input("Введіть номер дня тижня: "))
time = float(input("Введіть тривалість розмови: "))
price = 2.30
if day == 6 or day == 7:
    cost = time * price * 0.8
else:
    cost = time * price
print(round(cost, 2))