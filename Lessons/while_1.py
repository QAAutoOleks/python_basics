deposit_amount = float(input("Enter amount of deposit: "))
annual_rate = float(input("Enter rate: "))
desired_amount = float(input("Enter desire amount: "))

deposit_period = 0
while deposit_amount < desired_amount:
    deposit_period += 1
    deposit_amount = deposit_amount + deposit_amount * (annual_rate / 100)

print("Period:", deposit_period, "років")