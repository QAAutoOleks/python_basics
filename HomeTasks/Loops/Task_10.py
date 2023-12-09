a = int(input("Number: "))
simple = True
for i in range(1, a):
    if i > 1 and a % i == 0:
        simple = False
        break
if simple:
    print("Число просте")
else:                
    print("Число не просте")
