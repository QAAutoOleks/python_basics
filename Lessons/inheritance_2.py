class Horse:
    def say_hello(self):
        print('Я - кінь!')
class Eagle:
    def say_hello(self):
        print('Я - орел!')
class Pegasus(Eagle, Horse):  # який атрибут перший - 
    # той і буде виведений у консоль
    pass


p = Pegasus()
p.say_hello()