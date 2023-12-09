input_sentence = input("Введіть речення: ")
sentence_to_compare = input("Введіть речення для порівняння: ")
new_word = input("Введіть нове слово, яке потрібно додати в кінець речення: ")
input_word_to_remove = input("Введіть слово яке потрібно вилучити: ")


class Sentence:
# your code goes here
    sentence = ""
    def __init__(self, sentence):
        self.sentence = sentence
    def to_lower(self):
        self.sentence = self.sentence.lower()
    def add_word(self, word_to_add):
        self.sentence = self.sentence + word_to_add
    def remove_word(self, word_to_remove):
        if word_to_remove in self.sentence:
            self.sentence = self.sentence.replace(input_word_to_remove, "")
    def is_similar(self, sentence_to_compare):
        if sentence_to_compare.lower() == self.sentence.lower():
            return True
        else:
            return False

my_sentence = Sentence(input_sentence)
print(my_sentence.is_similar(sentence_to_compare))

my_sentence.add_word(new_word)
my_sentence.to_lower()
print(my_sentence.sentence)

my_sentence.remove_word(input_word_to_remove)
print(my_sentence.sentence)
