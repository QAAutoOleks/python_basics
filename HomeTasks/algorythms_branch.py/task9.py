mark = int(input("Оцінка: "))
if mark >= 90:
    res = "A"
elif mark < 90 and mark >= 80:
    res = "B"
elif mark < 80 and mark >= 70:
    res = "C"
elif mark < 70 and mark >= 60:
    res = "D"
else:
    res = "F"
print(res)