try:
    a = 10
    num = int(input("Enter num: "))
    print(a / num)
except ValueError:  # назву помилки можна скопіювати з консолі
    print("Invalid data")
except ZeroDivisionError:
    print("ZeroDivision")
except Exception:  # Exception ловить абсолютно всі помилки. Недолік - не можна побачити які
    print("Error")
else:  # else спрацює, якщо не спрацював попередній except
    print("Якийсь текст")
finally:  # finally завжди спрацьовує або після try, або після except
    print("Якийсь текст")