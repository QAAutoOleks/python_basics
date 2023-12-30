import pytest


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
