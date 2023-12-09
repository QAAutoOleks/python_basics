time = int(input("Enter time:"))
if ((time <= 5 and time >= 0) or time == 23):
    print("Good night!")
elif time > 5 and time < 11:
    print("Good morning!")
elif time >= 11 and time < 18:
    print("Good day!")
else:
    print("Good evening!")
