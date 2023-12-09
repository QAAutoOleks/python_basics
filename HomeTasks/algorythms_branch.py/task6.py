temp = int(input("Enter temperature: "))
if temp <= 0:
    print("A cold, isn't it?")
elif temp > 0 and temp < 10:
    print("Cool")
else:
    print("Nice weather we're having!")