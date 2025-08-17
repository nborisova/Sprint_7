import requests
from utils.constants import BASE_URL 
import random
import string
import allure

@allure.title('Проверка создания курьера с валидными данными')
@allure.description('Отправка данных на сервер методом POST')
def test_create_courier_with_valid_data():
    login = ''.join(random.choices(string.ascii_lowercase, k=5))
    courier_data = {
        "login": login,
        "password": "1234",
        "firstName": "natalia"
    }

    response = requests.post(BASE_URL + '/api/v1/courier', data=courier_data)

    assert response.status_code == 201
    assert response.json() == { "ok": True }

@allure.title('Проверка невозможности создания двух одинаковых курьеров')
@allure.description('Отправка набора двух одинаковых данных на сервер методом POST')
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

@allure.title('Проверка невозможности создания курьера без обязательного поля')
@allure.description('Отправка данных без обязательного поля на сервер методом POST')
def test_create_courier_with_incomlpete_data():
    incomlpete_courier_data = {
        "password": "1234",
        "firstName": "natalia"
    }

    response = requests.post(BASE_URL + '/api/v1/courier', data=incomlpete_courier_data)

    assert response.status_code == 400
    assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'
