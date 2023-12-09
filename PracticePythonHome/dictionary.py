capitals = {'USA':'Washington',
            'India':'New Dehli',
            'Ukraine':'Kyiv',
            'UK':'London'}

capitals.update({'Germany':'Berlin'}) # add
capitals.pop('India') # remove

# capitals.clear()
# print(capitals['Ukraine'])
# print(capitals.get('Germany'))
# print(capitals.keys()) - всі ключі
# print(capitals.values()) - всі значення
# print(capitals.items()) - всі зв'язки

for key, value in capitals.items():
    print(key, value)