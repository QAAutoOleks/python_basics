countries = {"Ukraine", "Poland"}
print(countries)
print("Ukraine" in countries)
print("US" in countries)

if "Ukraine" in countries:
    print("Україна є в переліку країн")
else:
    print("України немає в переліку країн")

if "US" in countries:
    print("Сполучені штати є  в переліку країн")
else:
    print("Сполучених штатів немає в переліку країн")
