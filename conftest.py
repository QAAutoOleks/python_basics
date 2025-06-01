import pytest
from modules.common.commissioning import Commissioning


@pytest.fixture
def addition_testing():
    addition_object = Commissioning()

    yield addition_object