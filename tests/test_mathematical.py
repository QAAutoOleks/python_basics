import pytest

@pytest.mark.commissioning_testing
def test_check_correct_returning(addition_testing):
    assert addition_testing.addition() == 1
