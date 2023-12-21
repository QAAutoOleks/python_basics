import pytest
import random


class RandomCreate:    

    def __init__(self):
        self.rand = None

    def rand_create(self):
        #self.rand = random.randint(1, 5)
        self.rand = 5

    def empty_rand(self):
        self.rand = 0


@pytest.fixture
def random_create():
    rand_obj = RandomCreate()
    rand_obj.rand_create()

    yield rand_obj  
    rand_obj.empty_rand()
