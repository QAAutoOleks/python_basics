import pytest
import random


class ListRandom:

    def __init__(self):
        self.list_random = []

    def list_create(self):
        for i in range(5):
            self.list_random.append(random.randint(1, 10))

    def list_clean(self):
        self.list_random = []


@pytest.fixture
def new_list_create():
    list_new = ListRandom()
    list_new.list_create()

    yield list_new

    list_new.list_clean