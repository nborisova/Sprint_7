import requests
from utils.constants import BASE_URL 
import random
import string


def test_create_courier():
    login = ''.join(random.choices(string.ascii_lowercase, k=5))
    courier_data = {
        "login": login,
        "password": "1234",
        "firstName": "natalia"
    }

    response = requests.post(BASE_URL + '/api/v1/courier', data=courier_data)

    assert response.status_code == 201
    assert response.json() == { "ok": True }

def test_create_courier_with_the_same_data():
    login = ''.join(random.choices(string.ascii_lowercase, k=5))
    courier_data = {
        "login": login,
        "password": "1234",
        "firstName": "natalia"
    }

    response = requests.post(BASE_URL + '/api/v1/courier', data=courier_data)
    response = requests.post(BASE_URL + '/api/v1/courier', data=courier_data)

    assert response.status_code == 409
    assert response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'

def test_create_courier_with_incomlpete_data():
    incomlpete_courier_data = {
        "password": "1234",
        "firstName": "natalia"
    }

    response = requests.post(BASE_URL + '/api/v1/courier', data=incomlpete_courier_data)

    assert response.status_code == 400
    assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'