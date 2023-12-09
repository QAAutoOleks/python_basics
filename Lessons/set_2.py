countries = {"Ukraine", "Poland", "China"}
print(countries)

countries.remove("China")  # remove - якщо в списку не буде "China", виникне помилка
countries.discard("Austria")  # discard - якщо в списку не буде "Austria", помилка не виникне
print(countries)