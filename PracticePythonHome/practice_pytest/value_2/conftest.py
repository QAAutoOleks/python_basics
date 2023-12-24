import pytest


class TestValue2:

    def __init__(self):
        self.value = 0
        self.value_string = "Empty"

    def create(self):
        self.value = 100

    def value_full(self):
        self.value_string = "Full"

    def clean(self):
        self.value = 0


@pytest.fixture
def value_test():
    value_object = TestValue2()
    value_object.create()
    value_object.value_full()

    yield value_object

    value_object.clean()