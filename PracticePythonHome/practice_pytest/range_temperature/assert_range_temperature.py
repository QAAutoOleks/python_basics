import pytest


def water_condition(t):
    if t < 0:
        return "Ice"
    elif t >= 0 and t < 100:
        return "Water"
    elif t > 100:
        return "Vapor"
    else:
        return "Error input"


@pytest.fixture
def water_tests():
    return water_condition()