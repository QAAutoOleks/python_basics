user = {"name": "Oleksandr"}
user["age"] = 100500

# додавання даних до словника
user["profession"] = "Automation QA"
print(user)

key = "country"
user[key] = "Ukraine"
print(user)

# перший спосіб отримання даних зі словника
# print(user['country'])
print(user[key])

# другий спосіб отримання даних зі словника
print(user.get('profession')) # 'profession' - key

# вилучення елемента
del user['profession']
print(user)