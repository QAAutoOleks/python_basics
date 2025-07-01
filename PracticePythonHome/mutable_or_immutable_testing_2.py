a = 3
b = a
c = a
print(id(b))
print(id(c))

a = "New name"
print(id(b))
