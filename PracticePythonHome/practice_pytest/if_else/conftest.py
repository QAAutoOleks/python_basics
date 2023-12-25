import pytest


class IfElse:

    def __init__(self, scores1=0, scores2=0):
        self.result1 = IfElse.scores_method(scores1)
        self.result2 = IfElse.scores_method(scores2)

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
        self.result1 = ""
        self.result2 = ""

@pytest.fixture
def if_else_method():
    if_else = IfElse(10, 20)

    yield if_else

    if_else.remove_result()
