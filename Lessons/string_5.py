str = str(input("Enter string: "))
str_len = len(str)

# мій варіант:
# print("String length =", str_len)

print(f"String '{str}' length = {str_len}")

print(f"First symbol of string is '{str[0]}'")
# slice
first_slice = slice(0, 1)
print(f"First symbol of string is '{str[first_slice]}'")


print(f"Last symbol of string is '{str[str_len - 1]}'")
# slice
last_slice = slice(-1, str_len)
print(f"Last symbol of string is '{str[last_slice]}'")
