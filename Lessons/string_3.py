user = {
    'name': 'Oleksandr',
    'age': 38,
    'profession': 'Automation QA',
    'country': 'Ukraine'
}


# схоже на printf
# print("Користувач з ім'ям {}, віком {}, проживає в {}.".format(user['name'], user['age'], user['country']))

# більш читабельний варіант
formatted_string = "Користувач з ім'ям {}, віком {}, проживає в {}."
print(formatted_string.format(user['name'], user['age'], user['country']))