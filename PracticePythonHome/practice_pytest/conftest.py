import pytest
import random


class RandomListCreate:    

    def __init__(self):
        self.list_random = []

    def list_create(self):
        for i in range(0, 5):
            self.list_random.append(random.randint(1, 5))
        return self.list_random

    def empty_list():
        self.list_random = []


@pytest.fixture
def random_list_create():
    random_list = RandomListCreate()
    random_list.list_create()

    yield random_list_create    
    random_list.empty_list()
