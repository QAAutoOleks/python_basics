import math

import pytest

@pytest.mark.do_not_doing
def test_check_correct_returning(addition_testing):
    assert addition_testing.addition() == 1


@pytest.mark.do_not_doing
def test_sum_string(addition_testing):
    assert addition_testing.make_string('Testing ', 'successful') == 'Testing successful'


@pytest.mark.commissioning_testing
def test_divisible_checking(addition_testing):
    assert addition_testing.divisible_by_5_and_7(71) == 2


@pytest.mark.commissioning_testing
def test_temperature_converter(addition_testing):
    assert addition_testing.converter_fahrenheit(71) == 21.666666666666668


@pytest.mark.commissioning_testing
def test_circle_area_calculator(addition_testing):
    assert addition_testing.circle_area_calculator(5) == math.pi * 5**2


@pytest.mark.commissioning_testing
def test_string_to_int(addition_testing):
    assert addition_testing.string_to_int('-123') == 123


@pytest.mark.commissioning_testing
def test_is_value_contained_in_list(addition_testing):
    assert addition_testing.is_value_contained(1) == True
    assert addition_testing.is_value_contained(0) == False
    assert addition_testing.is_value_contained(-1) == False


@pytest.mark.commissioning_testing
def test_common_divisor(addition_testing):
    assert addition_testing.common_divisor(3, 7) == 21


@pytest.mark.commissioning_testing
def test_type_validation_int(addition_testing):
    assert addition_testing.type_validation_int(10) == True
    assert addition_testing.type_validation_int(10.2) == False


@pytest.mark.commissioning_testing
def test_type_validation_str(addition_testing):
    assert addition_testing.type_validation_str('10') == True
    assert addition_testing.type_validation_str(10) == False