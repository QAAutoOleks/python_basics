import random

arr = []
for i in range(0, 10):
    arr.insert(i, random.randint(0, 10))
print(arr)  # весь масив
print(arr[5::2])  # елементи з 5 і до кінця з кроком 2
print(arr[4::-1])  # масив з 4 елементу у зворотному порядку
print(arr[len(arr) - 6::-1])  # масив з 4 елементу у зворотному порядку

if 0 in arr:  # пошук нуля серед всіх елементів
    print("Zero is here!")

if 0 in arr[0:4]:  # пошук нуля серед перших п'яти елементів
    print("Zero is here!")
