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
    list_results = []
    list_results.append(water_condition(-0.01))
    list_results.append(water_condition(0))
    list_results.append(water_condition(0.5))
    list_results.append(water_condition(99.9))
    list_results.append(water_condition(100))
    list_results.append(water_condition(101.9))
    list_results.append(water_condition(1000))
    return list_results