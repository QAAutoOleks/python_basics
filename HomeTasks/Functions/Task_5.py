import math


def cylinder_volume(r, h):
    volume = math.pi * r**2 * h
    return volume


def max_two(one, two):
    if one > two:
        return one
    else:
        return two


r1 = int(input("r1: "))
h1 = int(input("h1: "))
r2 = int(input("r2: "))
h2 = int(input("h2: "))

v1 = cylinder_volume(r1, h1)
v2 = cylinder_volume(r2, h2)
if v1 > v2:
    print("First is bigger")
else:
    print("Second is bigger")
