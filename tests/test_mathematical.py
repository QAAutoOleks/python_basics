import pytest

@pytest.mark.commissioning_testing
def test_check_correct_returning(addition_testing):
    assert addition_testing.addition() == 1

@pytest.mark.commissioning_testing
def test_sum_string(addition_testing):
    assert addition_testing.make_string('Testing ', 'successful') == 'Testing successful'
