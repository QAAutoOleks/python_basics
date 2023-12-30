import pytest


def test1(water_tests):
        assert water_condition(-1) == "Ice"
        # assert water_condition(0) == "Water"
        # assert water_condition(1) == "Water"
        # assert water_condition(99) == "Water"
        # assert water_condition(100) == "Vapor"
        # assert water_condition(101) == "Vapor"
