import time
n = int(input("Enter sec: "))
while n > 0:
    time.sleep(1)
    print(n)
    n -= 1