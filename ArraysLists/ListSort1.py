def myFunc(element):
    return len(element)

list1 = ["Text10", "Text100", "Text1000"]

list1.sort(reverse=True, key=myFunc)
print(list1)

def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)