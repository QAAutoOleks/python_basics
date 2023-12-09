from datetime import datetime

birthday_date = str(input("Enter date:"))
date = int(birthday_date[6:])
if (date % 12) == 0:
    print("Monkey")
elif (date % 12) == 1:
    print("Rooster")
elif (date % 12) == 2:
    print("Dog")
elif (date % 12) == 3:
    print("Pig")
elif (date % 12) == 4:
    print("Rat")
elif (date % 12) == 5:
    print("Bull")
elif (date % 12) == 6:
    print("Tiger")
elif (date % 12) == 7:
    print("Rabbit")
elif (date % 12) == 8:
    print("Dragon")
elif (date % 12) == 9:
    print("Snake")
elif (date % 12) == 10:
    print("Horse")
elif (date % 12) == 11:
    print("Goat")
