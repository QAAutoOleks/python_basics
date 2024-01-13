import pytest
import requests


class PetStore:
    id = 0

    def __init__(self, base_url):
        self.base_url = base_url
        PetStore.id += 1
        self.id = PetStore.id

    def post_method(self, extra_part_of_url, name_category, name_of_pet):
        body = {
            "id": self.id,
            "category": {"id": self.id, "name": name_of_pet},
            "name": name_category,
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}],
            "status": "available",
        }
        self.r_post = requests.post(self.base_url + extra_part_of_url, json=body)

    def put_method(self, extra_part_of_url, new_name):
        body = {
            "id": self.id,
            "category": {"id": self.id, "name": new_name},
            "name": "doggie",
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}],
            "status": "available",
        }
        self.r_put = requests.put(self.base_url + extra_part_of_url, json = body)


@pytest.fixture
def pet_crud():
    first_pet = PetStore("https://petstore.swagger.io/v2/")
    first_pet.post_method("pet", "Dogs", "Pes")
    first_pet.put_method("pet", "Mazik")

    yield first_pet
