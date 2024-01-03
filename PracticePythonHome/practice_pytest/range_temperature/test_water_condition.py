import pytest

@pytest.mark.only_second
def test_water(water_tests):
        assert water_tests[2] == "Water"


@pytest.mark.only_first
def test_water(water_tests):
        assert water_tests[1] == "Water"