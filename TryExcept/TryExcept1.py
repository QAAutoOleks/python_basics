num = None

while num is None:  # те ж саме, що <while num == None:>
    try:
        num = int(input("Enter num: "))
        print(num)
    except ValueError:  # назву помилки можна скопіювати з консолі
        print("Invalid data")