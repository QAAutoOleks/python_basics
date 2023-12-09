miles = float(input("Введіть кількість миль"))

# your code goes here
def convert_miles_to_km(miles):
    km = round((miles * 1.6), 2)
    return km

print(convert_miles_to_km(miles))