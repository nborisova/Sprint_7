import requests
from utils.urls import CREATE_COURIER_URL, LOGIN_COURIER_URL 
from utils.data import CREATE_COURIER_WITH_THE_SAME_DATA, CREATE_COURIER_WITH_INCOMPLETE_DATA
import random
import string
import allure


class TestCreateCourier:

    @allure.title('Проверка создания курьера с валидными данными')
    @allure.description('Отправка данных на сервер методом POST')
    def test_create_courier_with_valid_data(self):
        login = ''.join(random.choices(string.ascii_lowercase, k=5))
        courier_data = {
            "login": login,
            "password": "1234",
            "firstName": "natalia"
        }

        response = requests.post(CREATE_COURIER_URL, data=courier_data)

        assert response.status_code == 201
        assert response.json() == { "ok": True }

        response_for_login = requests.post(LOGIN_COURIER_URL, data={'login': login, 'password': '1234'})
        courier_id = response_for_login.json()["id"]
        response_for_delete = requests.delete(f'{CREATE_COURIER_URL}{courier_id}')

        assert response_for_delete.status_code == 200

    @allure.title('Проверка невозможности создания двух одинаковых курьеров')
    @allure.description('Отправка набора двух одинаковых данных на сервер методом POST')
    def test_create_courier_with_the_same_data(self):
        login = ''.join(random.choices(string.ascii_lowercase, k=5))
        courier_data = {
            "login": login,
            "password": "1234",
            "firstName": "natalia"
        }

        response = requests.post(CREATE_COURIER_URL, data=courier_data)
        response = requests.post(CREATE_COURIER_URL, data=courier_data)

        assert response.status_code == 409
        assert response.json()['message'] == CREATE_COURIER_WITH_THE_SAME_DATA

    @allure.title('Проверка невозможности создания курьера без обязательного поля')
    @allure.description('Отправка данных без обязательного поля на сервер методом POST')
    def test_create_courier_with_incomlpete_data(self):
        incomlpete_courier_data = {
            "password": "1234",
            "firstName": "natalia"
        }

        response = requests.post(CREATE_COURIER_URL, data=incomlpete_courier_data)

        assert response.status_code == 400
        assert response.json()['message'] == CREATE_COURIER_WITH_INCOMPLETE_DATA
