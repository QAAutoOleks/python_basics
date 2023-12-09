import math

cost = float(input("Вартість одного номеру: "))
period = int(input("Періодичність випуску (днів): "))

total_cost = math.floor(365 / period) * cost
print(total_cost)