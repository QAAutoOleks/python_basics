import pytest
import requests


class PetStore:
    id = 0

    def __init__(self, base_url):
        self.base_url = base_url
        PetStore.id += 1
        self.id = PetStore.id

    def post_method(self, name_category, name_of_pet):
        body = {
            "id": self.id,
            "category": {"id": self.id, "name": name_of_pet},
            "name": name_category,
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}],
            "status": "available",
        }
        self.r_post = requests.post(self.base_url, json=body)

    def put_method(self, new_name):
        body = {
            "id": self.id,
            "category": {"id": self.id, "name": new_name},
            "name": "doggie",
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}],
            "status": "available",
        }
        self.r_put = requests.put(self.base_url, json = body)

    def get_by_id(self):
        self.r_get_by_id = (requests.get(self.base_url + str(self.id))).json()


@pytest.fixture
def pet_crud():
    first_pet = PetStore("https://petstore.swagger.io/v2/pet/")
    first_pet.post_method("Dogs", "Pes")
    first_pet.put_method("Mazik")
    first_pet.get_by_id()

    yield first_pet
