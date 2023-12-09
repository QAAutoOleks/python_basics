# break =       used to terminate the loop entirely
# continue =    skips to the next iteration of the loop
# pass =        does nothing, acts as a placeholder

# while True:
#    name = input("Enter your name: ")
#    if name != "":
#        break

# for i in range(1, 21):
# if i == 13:
#   pass // 13 - не буде виведено в термінал
# else:
#   print(i)

phone_number = "123-456-7890"
for i in phone_number:
    if i == "-":
        continue
    print(i, end="")