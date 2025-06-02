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