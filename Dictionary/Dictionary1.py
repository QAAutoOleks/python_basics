people = {
    'user_1': {
        'name': 'John',
        'age': 27,
        'address': ('Seattle', 'Somestreet', 65),
        'grades': {'math': 5, 'physics': 2}
    },
    'user_2': {
        'surname': 'Doe',
        'name': 'Alex'
    }
}

print(people['user_1']['address'][1])
print(people['user_1']['address'])