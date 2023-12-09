word = "Oleksandr"
word = list(word)
print(word)
word.append('!')
result = ''.join(word)  # поєднує всі елементи масиву в строку
print(result)

text = 'orange, apple, strawberry'
fruit = text.split(' ')  # створює масив, елементи розділяються на кожному пробілі
print(fruit)