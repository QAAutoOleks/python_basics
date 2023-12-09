count = 0
real_weight = 0


while real_weight < 100:    
    weight = int(input("Enter weight: "))
    real_weight += weight
    if real_weight <= 100:
        count = count + 1    

print(count)
