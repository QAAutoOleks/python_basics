import pytest

@pytest.mark.checking_all_values
def test_water(water_tests):
        assert water_tests == [
            "Ice", 
            "Water", 
            "Water", 
            "Water",
            "Vapor",
            "Vapor",
            "Vapor"
        ]
