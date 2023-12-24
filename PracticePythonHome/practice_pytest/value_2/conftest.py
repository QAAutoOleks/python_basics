import pytest


class TestValue2:

    def __init__(self):
        self.value = 0

    def create(self):
        self.value = 100

    def clean(self):
        self.value = 0


@pytest.fixture
def value_test():
    value_object = TestValue2()
    value_object.create()

    yield value_object

    value_object.clean()