car_1 = input("Введіть марку автомобіля 1 ")
car_2 = input("Введіть марку автомобіля 2 ")
car_3 = input("Введіть марку автомобіля 3 ")


class Cars:
    # your code goes here
    list_of_cars = []


cars = Cars
cars.list_of_cars.append(car_1)
cars.list_of_cars.append(car_2)
cars.list_of_cars.append(car_3)
print("Список авто: {}".format(' та '.join(cars.list_of_cars)))
