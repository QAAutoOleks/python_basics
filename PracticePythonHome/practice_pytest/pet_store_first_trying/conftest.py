import pytest
import requests


class PetStore:
    id = 0

    def __init__(self, base_url):
        self.base_url = base_url
        PetStore.id += 1

    def post_method(self, extra_part_of_url, name_category, name_of_pet):
        body = {
            "id": PetStore.id,
            "category": {"id": PetStore.id, "name": name_of_pet},
            "name": name_category,
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}],
            "status": "available",
        }
        self.r = requests.post(self.base_url + extra_part_of_url, json=body)


@pytest.fixture
def post_pet():
    first_pet = PetStore("https://petstore.swagger.io/v2/")
    first_pet.post_method("pet", "Dogs", "Pes")

    yield first_pet
