import pytest


def test_first_test(id_sum_fix):
    assert id_sum_fix.id == 1

# разом із викликом методу id_sum_fix 
# створюється новий об'єкт,
# тому id_sum_fix.id == 2
def test_second_test(id_sum_fix):
    assert id_sum_fix.id == 2