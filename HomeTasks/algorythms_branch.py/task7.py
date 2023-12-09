speed_km = int(input("Speed in km/h: "))
speed_m = int(input("Speed in m/s: "))
if (speed_km * 1000 / 3600) > speed_m:
    print("First speed is higher")
elif (speed_km * 1000 / 3600) < speed_m:
    print("Second speed is higher")
else:
    print("Speeds are the same")