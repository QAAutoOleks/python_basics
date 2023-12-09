user = {
    'name': 'Oleksandr',
    'age': 38,
    'profession': 'Automation QA',
    'country': 'Ukraine'
}

# перевірка наявності ключа
print('age' in user)
print('company' in user)

if 'name' in user:
    print(user['name'])
else:
    print("Ключа 'name' немає в словнику")

if 'company' in user:
    print(user['company'])
else:
    print("Ключа 'company' немає в словнику")

# отримання списку всіх ключів
keys_list = user.keys()
print(keys_list)
print('age' in keys_list)

# видалення ключа
del user['age']
print(keys_list)

# зміна ключів неможлива!
# тому можна створювати копію потрібного значення,
# але із новим ключем
user['education'] = user['profession']
print(user)
del user['profession']
print(user)