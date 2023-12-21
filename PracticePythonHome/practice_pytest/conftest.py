import pytest
import random


class RandomListCreate:

    list_random = []

    def __init__(self):
        self.list_random = RandomListCreate.list_random


    def list_create(self):
        for i in range(0, 5):
            self.list_random.append(random.randint(1, 5))
        return list_random


rand = RandomListCreate()
print(rand.list_create())
