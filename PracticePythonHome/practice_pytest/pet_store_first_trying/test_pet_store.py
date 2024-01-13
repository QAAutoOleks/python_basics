import pytest


def test_check_status_code(post_pet):
    assert post_pet.r.status_code == 200