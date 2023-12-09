def deposit(dep, rate, year):
    res = dep + (dep * rate / 100) * year
    return res


dep = int(input("Dep: "))
rate = int(input("Rate: "))
year = int(input("Year: "))

print(round(deposit(dep, rate, year), 2))