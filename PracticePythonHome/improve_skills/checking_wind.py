wind = int(input()) # Don't change this line
status = "unset"
# Type your code below
if wind < 8:
    status = "Calm"
elif 8 <= wind <= 31:
    status = "Breeze"
elif 32 <= wind <= 63:
    status = "Gale"
else:
    status = "Storm"

# Don't change the line below
print(f"status = {status}")