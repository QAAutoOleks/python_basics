import pytest


def water_condition(t):
    if t < 0:
        return "Ice"
    elif t >= 0 and t < 100:
        return "Water"
    else:
        return "Vapor"


@pytest.fixture
def water_tests():
    assert water_condition(-1) == "Ice"
    assert water_condition(0) == "Water"
    assert water_condition(1) == "Water"
    assert water_condition(99) == "Water"
    assert water_condition(100) == "Vapor"
    assert water_condition(101) == "Vapor"