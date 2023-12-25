import pytest


class IfElse:

    value = 0

    def __init__(self, value):
        self.result = IfElse.scores_method(value)

    def scores_method(scores):
        if scores <= 10 and scores >= 0:
            return "D"
        elif scores <= 20:
            return "C"
        elif scores <= 30:
            return "B"
        elif scores <= 40:
            return "A"
        else:
            return "Incorrect input"

    def remove_result(self):
        self.result = ""

@pytest.fixture
def if_else_method():
    if_else = IfElse(IfElse.value)

    yield if_else

    IfElse.value += 10
