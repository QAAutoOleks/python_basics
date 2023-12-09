class Dog:
    name = None
    age = None
    isHappy = None

    def __init__(self, name, age, isHappy):
        self.name = name
        self.age = age
        self.isHappy = isHappy


dog1 = Dog("Psina", 100, True)
print(dog1.name)
#  dog2 = Dog()
