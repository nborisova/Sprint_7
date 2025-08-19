import requests
from utils.urls import LOGIN_COURIER_URL, CREATE_COURIER_URL
from utils.generate_courier_data import register_new_courier_and_return_login_password 
from utils.data import LOGIN_COURIER_WITHOUT_REQUIRED_FIELD, LOGIN_COURIER_WITH_INVALID_DATA
import allure


class TestLoginCourier:

    @allure.title('Возможность курьеру залогиниться с валидными данными')
    @allure.description('Отправка валидных данных на сервер методом POST')
    def test_login_courier_with_valid_data(self):
        login, password, first_name = register_new_courier_and_return_login_password()

        response = requests.post(LOGIN_COURIER_URL, data={'login': login, 'password': password})

        assert response.status_code == 200
        assert 'id' in response.json()
    
        courier_id = response.json()["id"]
        response_for_delete = requests.delete(f'{CREATE_COURIER_URL}{courier_id}')

        assert response_for_delete.status_code == 200

    @allure.title('Невозможность залогиниться без заполнения одного из обязательных полей')
    @allure.description('Отправка только логина на сервер методом POST')
    def test_login_courier_without_password(self):
        login, password, first_name = register_new_courier_and_return_login_password()

        response = requests.post(LOGIN_COURIER_URL, data={'login': login, 'password': ''})

        assert response.status_code == 400
        assert response.json()['message'] == LOGIN_COURIER_WITHOUT_REQUIRED_FIELD

    @allure.title('Невозможность залогиниться несуществующим пользователем')
    @allure.description('Отправка несуществующих данных на сервер методом POST')
    def test_login_courier_with_invalid_data(self):
        response = requests.post(LOGIN_COURIER_URL, data={'login': 'login', 'password': 'password'})

        assert response.status_code == 404
        assert response.json()['message'] == LOGIN_COURIER_WITH_INVALID_DATA
