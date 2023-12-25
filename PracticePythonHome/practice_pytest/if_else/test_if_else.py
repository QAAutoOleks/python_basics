import pytest


def test_if_else1(if_else_method):
    assert if_else_method.result == 'D'

def test_if_else2(if_else_method):
    assert if_else_method.result == 'D'

def test_if_else3(if_else_method):
    assert if_else_method.result == 'C'