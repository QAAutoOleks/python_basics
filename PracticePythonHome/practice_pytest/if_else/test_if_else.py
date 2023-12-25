import pytest


def test_if_else1(if_else_method):
    assert if_else_method.result1 == 'D'

def test_if_else2(if_else_method):
    assert if_else_method.result2 == 'C'