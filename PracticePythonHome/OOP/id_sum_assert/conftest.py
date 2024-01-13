import pytest


class IdSum:
    
    id = 0

    def __init__(self):
        IdSum.id += 1
        self.id = IdSum.id

    def second_method(self):
        return self.id

    def third_method(self):
        return self.id


@pytest.fixture
def id_sum_fix():
    id_sum = IdSum()
    id_sum.second_method()
    id_sum.third_method()
    yield id_sum