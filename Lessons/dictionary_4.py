user = {
    'name': 'Oleksandr',
    'age': 38,
    'profession': 'Automation QA',
    'country': 'Ukraine'
}

# уникнення помилок
# .get - не виникне помилка,
# проте у змінну 'years_old' запишеться None
years_old = user.get('years_old')
if years_old is None:
    print("Ключ 'years_old' відсутній")
else:
    print(years_old)

if 'years_old' in user:
    print(years_old)
else:
    print("Ключ 'years_old' відсутній")