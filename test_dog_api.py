# Тест на получение списка всех пород собак
import requests
import pytest

@pytest.mark.parametrize("breed", ["hound", "retriever", "bulldog"])
def test_get_all_breeds(breed):
    response = requests.get(f"https://dog.ceo/api/breeds/list/all")
    data = response.json()
    assert response.status_code == 200
    assert breed in data["message"]

# Тест на получение случайной фотографии собаки
import requests
import pytest

def test_get_random_dog_image():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    data = response.json()
    assert response.status_code == 200
    assert data["status"] == "success"
    assert data["message"].endswith(".jpg")

# Тест на получение фотографии определенной породы собаки
import requests
import pytest

@pytest.mark.parametrize("breed", ["husky", "labrador", "bulldog"])
def test_get_breed_image(breed):
    response = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random")
    data = response.json()
    assert response.status_code == 200
    assert data["status"] == "success"
    assert data["message"].endswith(".jpg")

# Тест на получение списка подпороды для заданной породы
import requests
import pytest

@pytest.mark.parametrize("breed", ["collie", "poodle", "bulldog"])
def test_get_subbreeds(breed):
    response = requests.get(f"https://dog.ceo/api/breed/{breed}/list")
    data = response.json()
    assert response.status_code == 200
    assert breed in data["message"]

# Тест на получение информации о случайной фотографии собаки и её породе
import requests
import pytest

def test_get_random_dog_info():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    data = response.json()
    assert response.status_code == 200
    assert data["status"] == "success"
    assert data["message"].endswith(".jpg")

    breed = data["message"].split("/")[-2]
    response_breed = requests.get(f"https://dog.ceo/api/breed/{breed}/list")
    data_breed = response_breed.json()
    assert response_breed.status_code == 200
    assert breed in data_breed["message"]