import pytest


class IfElse:

    def __init__(self, scores):
        self.result = IfElse.scores_method(scores)

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
    val = int(input("Enter value: "))
    if_else = IfElse(val)

    yield if_else

    if_else.remove_result()
