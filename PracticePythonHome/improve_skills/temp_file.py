import pytest


@pytest
def test_sum_two_numbers():
    a, b = 2, 7
    assert a + b == 9