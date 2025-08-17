import requests
from utils.constants import BASE_URL 
import pytest
import allure


data = [
    {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK"
        ]
    },
    {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK",
            "GREY"
        ]
    },
    {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha"
    }
]

@allure.title('Создание заказа с разными вариантами цветов самоката и без его указания')
@allure.description('Отправка набора данных на сервер методом POST')
@pytest.mark.parametrize('data', data)
def test_create_order(data):
    response = requests.post(BASE_URL + '/api/v1/orders', json=data)

    assert response.status_code == 201
    assert 'track' in response.json()
