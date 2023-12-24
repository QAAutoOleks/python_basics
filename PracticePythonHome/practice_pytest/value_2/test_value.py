import pytest


@pytest.mark.is_value_100
def test_value_100(value_test):
    assert value_test.value == 100


@pytest.mark.what_value_string
def test_value_string(value_test):
    assert value_test.value_string == "Full"