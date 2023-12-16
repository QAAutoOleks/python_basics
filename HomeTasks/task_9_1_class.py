windows_count = int(input("Введіть кількість вікон "))
flors_count = int(input("Введіть кількість поверхів "))


class Building:
    # your code goes here
    windows_count = 0
    flors_count = 0
    def building_counts(self, windows, flors):
        Building.windows_count = windows
        Building.flors_count = flors



building = Building()
building.building_counts(windows_count, flors_count)
print("Загальна кількість вікон {}".format(building.windows_count * building.flors_count))
