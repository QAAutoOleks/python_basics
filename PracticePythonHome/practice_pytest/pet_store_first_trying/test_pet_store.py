import pytest


def test_check_post(pet_crud):
    assert pet_crud.r_post.status_code == 200
    
def test_check_put(pet_crud):
    assert pet_crud.r_put.status_code == 200