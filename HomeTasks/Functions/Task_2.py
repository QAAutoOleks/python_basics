def year_check(year):
    if year % 4 == 0:
        print("Рік високосний")
    else:
        print("Рік невисокосний")


year_input = int(input("Enter year"))
year_check(year_input)
